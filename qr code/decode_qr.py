from pyzbar.pyzbar import decode
from PIL import Image

decodeQR = decode(Image.open("qr code//datascience.png"))
print(decodeQR[0].data.decode('ascii'))

