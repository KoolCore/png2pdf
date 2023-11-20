import os
from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# 遍历指定文件夹下的所有图片文件
def get_image_files(folder):
    image_extensions = ['.png', '.jpg', '.jpeg']
    image_files = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(os.path.join(root, file))
    return image_files

# 合并图片为PDF
def images_to_pdf(image_files, output_pdf):
    c = canvas.Canvas(output_pdf, pagesize=letter)
    for image_file in image_files:
        img = Image.open(image_file)
        img_width, img_height = img.size
        c.setPageSize((img_width, img_height))
        c.drawImage(image_file, 0, 0, width=img_width, height=img_height)
        # 添加水印
        c.setFont("Helvetica", 82)
        c.setFillGray(0)  # 使用黑色字体
        c.drawCentredString(img_width / 2, img_height / 5, "iKOOLCORE") #指定水印文字，仅限英文字符。
        c.showPage()
    c.save()

if __name__ == '__main__':
    input_folder = "E:\png2pdf"
    output_pdf = "E:\png2pdf\生成的PDF文件.pdf"
    image_files = get_image_files(input_folder)
    image_files.sort(key=lambda x: Image.open(x).size, reverse=True)  # 按清晰度排序
    images_to_pdf(image_files, output_pdf)
    print(f"PDF文件 {output_pdf} 已完成。")
