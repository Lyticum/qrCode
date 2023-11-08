import qrcode #You have install qrcode libary with -pip install qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Website')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("QR.png")


