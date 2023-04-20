import qrcode

def qr_generator(text):
    data = qrcode.QRCode(
        version=1,
        error_correction=qrcode.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    data.add_data(text)
    data.make(fit=True)
    img = data.make_image(fill_color = 'black', back_color = 'white')
    img.save('Qrcodeimage001.jpg')

url = input("Enter the url : ")
qr_generator(url)