class Help(object):
    ADD_CONTACT_TXT = "🌍 <b><u>How to add a contact in this bot?</u></b>\n\n<i>A contact can be added to this bot in a " \
                      "special format, mentioned  below. If any errors in the format, the bot wont be able to " \
                      "add the contact to it's database, results popping up an error message.</i>\n\n<b>📚 Format:</b>\n" \
                      "<code>/add name dept mobile Ext.No mail emp\n\nEg: /add David-John-S Electrical +91568455788 " \
                      "davidjohn@gmail.com 255</code>\n\n<b>💡 Tips:</b>\n<i>Spaces between a full name should be " \
                      "replaced by the '-' hyphen symbol (David-John-S). Phone numbers need to be added " \
                      "in an international format. All the parameters in the command should be separated by spaces.</i>" \
                      "<b><strike>This command can only execute by the admins of this bot.</strike></b>"

    DEL_CONTACT_TXT = "🌍 <b><u>How to delete a contact in this bot?</u></b>\n\n<i>Using a special command, we can" \
                      " remove one or multiple contacts from this bot. The Format is mentioned below. If any errors" \
                      " in the format, results popping up an error message.</i>\n\n<b>📚 Format:</b>\n<code>/delete " \
                      "emp1 emp3 emp3 ... emp'n'\n\nEg: /delete 234 255 327 213 621</code>\n\n<b>💡 Tips:</b>\n<i>" \
                      "Employee codes need to be placed one after another separated by space followed by the delete" \
                      " command. We can delete 'n' number of contacts by executing a single command.</i><b><strike> " \
                      "This command can only execute by the admins of this bot</strike></b>"

    ADD_EMAIL_TXT = "🌍 <b><u>How to update an email id in this bot?</u></b>\n\n<i>Using a special command, we " \
                    "can update the existing email address in this bot. Format is mentioned below. If any errors" \
                    " in the format, results popping up an error message.</i>\n\n<b>📚 Format:</b>\n<code>/email emp " \
                    "email@mail.com\n\nEg: /email 255 john@gmail.com</code>\n\n<b>💡 Tips:</b>\n<i>An existing contact" \
                    " can only be able to update the email id.</i><i><strike>This command can be run by a user for " \
                    "updating their own email id.</strike></i>"

    ADD_MOBILE_TXT = "🌍 <b><u>How to update a mobile number in this bot?</u></b>\n\n<i>Using a special command, we " \
                     "can update the existing mobile number in this bot. Format is mentioned below. If any errors" \
                     " in the format, results popping up an error message.</i>\n\n<b>📚 Format:</b>\n<code>/mobile " \
                     "emp mobile1 mobile2\n\nEg: /mobile +91958875487 +916854788544</code>\n\n<b>💡 Tips:</b>\n<i>" \
                     "An existing contact can only be able to update the mobile number. Up to two mobile numbers can " \
                     "be added to a contact using this command. Numbers need to be separated by a space.</i><i>" \
                     "<strike>This command can be run by a user for updating their own mobile number.</strike></i>"

    ADD_PHOTO_TXT = "🌍 <b><u>How to update thumbnail photo in this bot?</u></b>\n\n<i>Using a special command, we " \
                    "can update the existing contact photo in this bot. Format is mentioned below. If any errors" \
                    " in the format, results popping up an error message.</i>\n\n<b>📚 Format:</b>\n<code>/photo emp.no"\
                    "\n\nEg: /photo 255</code>\n\n<b>💡 Tips:</b>\n<i>Send a relevant photo to the bot chat, as a reply"\
                    " to the above photo, give the above command. Then the bot will update thumbnail image with the"\
                    " uploaded photo.</i><b><strike>This command can only execute by the admins of this bot.</strike></b>"

    ADD_EXTENSION_TXT = "🌍 <b><u>How to update extension number in this bot?</u></b>\n\n<i>Using a special command, " \
                        "we can update the existing extension number in this bot. Format is mentioned below. If any" \
                        " errors in the format, results popping up an error message.</i>\n\n<b>📚 Format:</b>\n<code>" \
                        "/extension emp.no extension_No\n\nEg: /extension 254 04842544858</code>\n\n<b>💡 Tips:</b>\n" \
                        "<i>Extension number is the number which can be dialed from outside the organization. It is " \
                        "the work phone number, basically a landline number. Add this number in a global format that "\
                        "can be in a 'click and called' method.<strike>This command can be run by a user for updating" \
                        " their own extension number.</strike></i>"

    FIND_ADMINS_TXT = "🌍 <b><u>How to find An admin of this bot?</u></b>\n\n<i>Using a special command, we can find" \
                      " an admin of this bot.</i>\n\n<b>📚 Format:</b>\n<code>/admins</code>\n\n<b>💡 Tips:</b>\n" \
                      "<i>Some of the functions of this bot can only be done with the help of admins. Some users of " \
                      "this bot are promoted as admins to add or update the potential datas of employees of the"\
                      " organization. By running the above command will get the name list of admins with profile link,"\
                      " so that the users can directly contact nearest admin for updating their potential data.<strike>"\
                      " This command can be run by a user for finding Admins of this bot</strike></i>"

    IMPORT_DATA_TXT = "🌍 <b><u>How to import contacts to the bot database?</u></b>\n\n<i>Using a special command, " \
                      "we can import contact details of the employees to the bot database. By uploading and extracting "\
                      "a CSV file will import the contents of the file to the bot database. A special formatting is" \
                      " used to identify the database fields.</i>\n\n<b>📚 Format:</b>\n<code>/load</code>\n\n<b>CSV " \
                      "Header:\nname,dept,mobile,extension,mail,emp,thumb_url</b>\n\n<b>💡 Tips:</b>\n<i>Prepare a CSV "\
                      "file with the above header and data rows. Upload the prepared CSV file to the bot chat. As a "\
                      "reply to the uploaded CSV file, give the command. Then the bot will extract all the datas in "\
                      "the uploaded CSV file and save it to the bot database. This is the easiest method to import "\
                      "a huge data to the bot's database in simple.</i> <b><strike>This command can only execute by " \
                      "the Super admins of this bot.</strike></b>"

    BROADCAST_MSG_TXT = "🌍 <b><u>How to Broadcast messages to the bot users?</u></b>\n\n<i>Using a special command, " \
                        "<strike>sudo users</strike> of this bot can broadcast messages / medias to the bot users.</i>" \
                        "\n\n<b>📚 Format:</b>\n<code>/send</code>\n\n<b>💡 Tips:</b>\n<i>Prepare a Text or " \
                        "media message in the bot chat. After drafting and reviewing the same, as a reply to the above " \
                        "message, give the command.</i> <b><strike>This command can only execute by the Super admins " \
                        "of this bot.</strike></b>"

    LIST_USERS_TXT = "🌍 <b><u>How to view the subscribers list of this bot?</u></b>\n\n<i>Using a special command, " \
                     "<strike>sudo users</strike> of this bot can view the subscribers count of this bot.</i>\n\n" \
                     "<b>📚 Format:</b>\n<code>/users</code>\n\n<b>💡 Tips:</b>\n<i>Just send the command in the bot " \
                     "chat, It will take some time to fetch all the bot users list. After completing the operation, " \
                     "the bot will list the names of the active users with total count.</i><b><strike>This command " \
                     "can only execute by the Super admins of this bot.</strike></b>"

    HOW_TO_DO_TXT = "🌍 <b><u>How to search a contact in this bot?</u></b>\n\n<b>📚 Procedure:</b>\n\n1️⃣ <i>Tap the button "\
                    "<b>Search Here</b>\n\n2️⃣ Search by the\n     🔹Name\n     🔹Department\n     🔹Phone number\n\n" \
                    "3️⃣ Tap the result\n\n<b>💡 Tips:</b>\nThe results will be delivered only to <strike><b>those who " \
                    "are the member </b></strike> of the organization's official channel or group.</i>"


