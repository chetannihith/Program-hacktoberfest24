import qrcode

def generate_qr_code(data, file_name="qrcode.png", size=10, border=4):
    # Create a QR code instance with specified settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create and save the image
    img = qr.make_image(fill="black", back_color="white")
    img.save(file_name)
    print(f"QR code saved as {file_name}")

# Get user input for QR code content
data = input("Enter the data or URL for the QR code: ")
file_name = input("Enter the output file name (e.g., qrcode.png): ")

# Generate the QR code
generate_qr_code(data, file_name)
