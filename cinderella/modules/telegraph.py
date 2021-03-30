def upload(client, message):

    message_id = (app.send_message(text="Downloading & Uploading...."

    chat_id = message.from_user.id, reply_to_message_id=message.message_id)).message_id

    file_name = f'{str(message.from_user.id)}.jpg'

    message.download(file_name=file_name)

    files = {'files': open(f'downloads/{file_name}', 'rb')}

    r = requests.post("https://telegra.ph/upload", files=files)

    info = r.json()

    if info[0].get("error"):

        return message.reply_text("Failed to upload. Reason: {err}".format(err=info[0].get("error")))

    url = "https://telegra.ph" + info[0].get("src")

    app.edit_message_text(text=url, chat_id=message.from_user.id, message_id=message_id)

    os.remove(f'downloads/{file_name}')
