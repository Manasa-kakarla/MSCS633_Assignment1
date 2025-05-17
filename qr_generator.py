import qrcode

def generate_qr_code(data, filename="biox_qr.png"):
    """
    Generates a QR code image file from the provided data.
    
    :param data: String to encode into the QR code
    :param filename: Name of the file to save the QR code image
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"✅ QR code saved as '{filename}'")

if __name__ == "__main__":
    data = input("Enter the data (URL/text) for the QR code: ")
    filename = input("Enter the filename to save (e.g., biox_qr.png): ")
    generate_qr_code(data, filename)

