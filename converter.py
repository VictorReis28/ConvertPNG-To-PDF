import fitz
from PIL import Image
import io

pdf_path = "fatura.pdf"

doc = fitz.open(pdf_path)

for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    
    mat = fitz.Matrix(300/72, 300/72)
    pix = page.get_pixmap(matrix=mat)
    
    img_data = pix.tobytes("png")
    img = Image.open(io.BytesIO(img_data))
    
    img.save(f"pagina_{page_num+1}.png", "PNG")

doc.close()

print("Conversão concluída!")
