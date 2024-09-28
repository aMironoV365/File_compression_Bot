import aspose.pdf as ap
import io
from aiogram import F
from aiogram.types import BufferedInputFile

from loader import dp, bot
from aiogram import types


def compress_pdf(pdf_bytes):
    # Загрузить PDF-файл из байтового потока
    pdf_document = ap.Document(io.BytesIO(pdf_bytes))

    # Создайте объект класса OptimizationOptions
    pdf_optimize_options = ap.optimization.OptimizationOptions()

    # Включить сжатие изображений
    pdf_optimize_options.image_compression_options.compress_images = True

    # Установите качество изображения
    pdf_optimize_options.image_compression_options.image_quality = 50

    # Сжать PDF
    pdf_document.optimize_resources(pdf_optimize_options)

    # Сохраните сжатый PDF в байтовый поток
    output_pdf = io.BytesIO()
    pdf_document.save(output_pdf)
    output_pdf.seek(0)
    return output_pdf


@dp.message(F.document.mime_type == "application/pdf")
async def handle_document(message: types.Message):
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    try:
        document_file = await bot.download_file(file_path)
        compressed_pdf = compress_pdf(document_file.read())
        await message.reply_document(BufferedInputFile(compressed_pdf.read(), filename="compressed_pdf.pdf"))
    except Exception as e:
        await message.reply(f"Ошибка при загрузке файла: {e}")
