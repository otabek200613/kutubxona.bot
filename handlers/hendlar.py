@dp.message_handler()
async def qaytish(message: types.Message):
    fayllar = [

    ]

    for f in fayllar:
        if f["type"] == "document":
            await message.answer_document(document=f["id"])
        elif f["type"] == "audio":
            await message.answer_audio(audio=f["id"])
        elif f["type"] == "video":
            await message.answer_video(video=f["id"])