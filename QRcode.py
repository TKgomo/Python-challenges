import qrcode

data = "Don't forget to subscrib"

img = qrcode.make(data)
img.save('/Users/TshegofatsoKgomo/Documents/Capitec Work/Work Python/myqrcode.png')

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'black',back_color ="white")


##### Decoding the qr code:
# Getting data written in the QR Code.
