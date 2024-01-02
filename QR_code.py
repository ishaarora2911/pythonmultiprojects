import qrcode as qr
from PIL import Image
qrr=qr.QRCode(version=1,
              error_correction=qr.constants.ERROR_CORRECT_H,
              box_size=10,
              border=4,
              )
# img=qr.make(" https://chat.openai.com/c/7b80e13a-631e-4348-8811-34413cd8a72c")
# img.save("chatgptqr.png")
qrr.add_data("https://www.youtube.com/watch?v=9exrSM6tiWg")
qrr.make(fit=True)
img=qrr.make_image(fill_color="red",back_color="black")
img.save("chatgptqr1.png")
