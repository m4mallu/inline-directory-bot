#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : inline-directory-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/inine-directory-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

import os
import csv
import codecs
import asyncio
import threading
from pyrogram.errors import FloodWait
from sqlalchemy import create_engine, func
from sqlalchemy import Column, Numeric, TEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


if bool(os.environ.get("ENV", False)):
    from sample_config import Config
else:
    from config import Config


def start() -> scoped_session:
    engine = create_engine(Config.DB_URI, client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

INSERTION_LOCK = threading.RLock()

class Directory(BASE):
    __tablename__ = "directory"
    # Seven columns with employ code as the primary key
    name = Column(TEXT)
    dept = Column(TEXT)
    mobile = Column(Numeric)
    extension = Column(Numeric)
    mail = Column(TEXT)
    emp = Column(Numeric, primary_key=True)
    thumb_url = Column(TEXT)

    def __init__(self, name, dept, mobile, extension, mail, emp, thumb_url):
        self.name = name
        self.dept = dept
        self.mobile = mobile
        self.extension = extension
        self.mail = mail
        self.emp = emp
        self.thumb_url = thumb_url

Directory.__table__.create(checkfirst=True)


# ----------------------------------- query for a single contact --------------------- #
async def query_emp(emp):
    try:
        query = SESSION.query(Directory).filter(Directory.emp == emp).first()
        return query
    finally:
        SESSION.close()


# ----------------------------------- query contact details --------------------------- #
async def query_msg(string):
    try:
        query = SESSION.query(Directory).filter(func.lower(Directory.name).contains(func.lower(string)))
        return query
    except FloodWait as e:
        await asyncio.sleep(e.x)
    finally:
        SESSION.close()


# ------------------------------------ Add contact details ----------------------------- #
async def add_user(name, dept, mobile, extension, mail, emp, thumb_url):
    with INSERTION_LOCK:
        msg = SESSION.query(Directory).get(emp)
        if not msg:
            usr = Directory(name, dept, mobile, extension, mail, emp, thumb_url)
            SESSION.add(usr)
            SESSION.commit()
        else:
            pass


# ------------------------------------- update contact details -------------------------- #
async def update_user(name, dept, mobile, extension, mail, emp):
    with INSERTION_LOCK:
        try:
            SESSION.query(Directory).filter(Directory.emp == emp).update({'name': name,
                                                                          'dept': dept,
                                                                          'mobile': mobile,
                                                                          'extension': extension,
                                                                          'mail': mail,
                                                                          'emp': emp})
        finally:
            SESSION.commit()


# -------------------------------------- update thumbnail image ------------------------- #
async def update_thumb(emp, url):
    with INSERTION_LOCK:
        try:
            SESSION.query(Directory).filter(Directory.emp == emp).update({'thumb_url': url})
        finally:
            SESSION.commit()


# ---------------------------------- write csv file to db ------------------------------- #
async def load_db(file_name):
    with INSERTION_LOCK:
        try:
            with codecs.open(file_name, 'r', encoding='utf-8', errors='ignore') as csv_file:
                csv_data = csv.reader(csv_file, delimiter=',')
                next(csv_data, None)  # Skip the first raw(header)
                for i in csv_data:
                    record = Directory(**{
                        'name': i[0],
                        'dept': i[1],
                        'mobile': i[2],
                        'extension': i[3],
                        'mail': i[4],
                        'emp': i[5],
                        'thumb_url': i[6]
                    })
                    # find and replace existing rows ( except employ code & thumbnail image )
                    status = SESSION.query(Directory).filter(Directory.emp == record.emp).first()
                    if bool(status) is True:
                        SESSION.query(Directory).filter(
                            Directory.emp == record.emp).update({'name': record.name,
                                                                 'dept': record.dept,
                                                                 'mobile': record.mobile,
                                                                 'extension': record.extension,
                                                                 'mail': record.mail
                                                                 })
                    else:
                        SESSION.add(record)
                    SESSION.commit()
        except Exception:
            SESSION.rollback()
            return Exception
        finally:
            SESSION.close()


# -------------------------------- mass delete contacts -------------------------------- #
async def mass_delete(emp_list):
    for i in emp_list:
        record = SESSION.query(Directory).filter(Directory.emp == i)
        if record:
            try:
                SESSION.query(Directory).filter(Directory.emp == i).delete()
                SESSION.commit()
            except Exception:
                pass
        else:
            pass


# ------------------------- update extension number ---------------------------- #
async def update_extension(emp, value):
    record = SESSION.query(Directory).filter(Directory.emp == emp).first()
    if record:
        try:
            SESSION.query(Directory).filter(Directory.emp == emp).update({'extension': value})
        finally:
            SESSION.commit()
    else:
        raise Exception
