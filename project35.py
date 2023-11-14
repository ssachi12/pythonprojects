import qrcode
import os

def generate_qr_code(name, phone, email, company, website):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )


    qr.add_data(f"{name}\n{phone}\n{email}\n{company}\n{website}")


    qr_image = qr.make_image(fill_color="black", back_color="white")


    qr_image.save("qr_code.png")


name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email address: ")
company = input("Enter your company name: ")
website = input("Enter your website URL: ")


generate_qr_code(name, phone, email, company, website)


print("QR code generated successfully!")


os.system(f"start qr_code.png")
