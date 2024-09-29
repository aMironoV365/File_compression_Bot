import aspose.pdf as ap
import io
from aiogram import F
from aiogram.types import BufferedInputFile
from loader import dp, bot
from aiogram import types
from config_data.logger_config import setup_logging

setup_logging()


async def compress_pdf(pdf_bytes: bytes) -> io.BytesIO:
    """
    Сжимает PDF-документ, используя библиотеку Aspose.PDF.

    Аргументы:
    - pdf_bytes (bytes): Байты исходного PDF-документа.

    Возвращает:
    - io.BytesIO: Байты сжатого PDF-документа.
    """
    pdf_document = ap.Document(io.BytesIO(pdf_bytes))
    pdf_optimize_options = ap.optimization.OptimizationOptions()

    pdf_optimize_options.image_compression_options.compress_images = True
    pdf_optimize_options.image_compression_options.image_quality = 50
    pdf_document.optimize_resources(pdf_optimize_options)

    output_pdf = io.BytesIO()
    pdf_document.save(output_pdf)
    output_pdf.seek(0)
    return output_pdf


@dp.message(F.document.mime_type == "application/pdf")
async def handle_document(message: types.Message) -> None:
    """
    Обрабатывает сообщение с PDF-документом, сжимает его и отправляет обратно.

    Аргументы:
    - message (types.Message): Сообщение с PDF-документом.
    """
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path

    try:
        document_file = await bot.download_file(file_path)
        compressed_pdf = await compress_pdf(document_file.read())
        await message.reply_document(BufferedInputFile(compressed_pdf.read(), filename="compressed_pdf.pdf"))
    except Exception as e:
        await message.reply(f"Ошибка при загрузке файла: {e}")
