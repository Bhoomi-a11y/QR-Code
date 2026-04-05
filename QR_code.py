import qrcode as qr
img = qr.make("https://www.linkedin.com/in/bhoomi-raikwar-a11y/")
img.save("Linkdin_Profile.png")
print("QR Code generated successfully!")