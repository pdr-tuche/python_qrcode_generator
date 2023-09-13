import qrcode

# Função para gerar um QR code a partir de um link
def generate_qr_code(link, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Link que você deseja transformar em QR code
link_to_generate = "https://forms.gle/rWtoBzFizpS2S1CM7"
# Nome do arquivo de saída
output_filename = "qrcode_example.png"

generate_qr_code(link_to_generate, output_filename)
print(f"QR code gerado com sucesso e salvo em '{output_filename}'.")

