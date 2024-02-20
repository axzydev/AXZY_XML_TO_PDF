import qrcode
import base64
from io import BytesIO

def generate_qr_code_base64(data, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    base64_image = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return base64_image