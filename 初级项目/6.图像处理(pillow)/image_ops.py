from PIL import ImageFont, ImageDraw, Image


def read_show_pic(img_path):
    """读取和显示图片"""
    img = Image.open(img_path)
    img.show() # PIL的show() 方法速度很慢，可能需要等待几秒
    return img

def get_thumbnail(img_path):
    """获得图片缩略图"""
    img = Image.open(img_path)
    img.thumbnail((128,128)) # 缩略图尺寸128 x 128
    return img

def compress_image(source_path, dest_path):
    """压缩图片大小"""
    with Image.open(source_path) as img:
        if img.mode != "RGB":
            img = img.convert("RGB")
        img.save(dest_path, "JPEG", optimize=True, quality=80)

def enhance(img_path):
    """图像增强（锐化）"""
    with Image.open(img_path) as img:
        from PIL import ImageEnhance
        enhancer = ImageEnhance.Sharpness(img)
        for i in range(4):
            factor = i / 2.0 # factor = 0 是模糊 ， 1是原图， 超过1是锐化
            enhancer.enhance(factor).show(title=f"Sharpness {factor:f}") 
        

    
def draw_text(img_path,text,pos):
    """在pos位置绘制txt"""
    img = Image.open(img_path)
    # 在PIL格式的图像上绘制中文文字
    font_path = "SourceHanSerifSC-VF.ttf"# 设置字体路径 ttf文件或otf文件
    #font_path = "AdobeSongStd-Light.otf"  
    font = ImageFont.truetype(font_path, size=100)  # 设置字体和大小
    draw = ImageDraw.Draw(img)  # 创建画笔
    color = (0, 255, 0)  # 文字颜色
    draw.text(pos, text, color, font=font)  # 绘制文字
    return img 

if __name__ == '__main__':
    img_path = 'pics/pic.jpg'
    
    # 读取和显示
    read_show_pic(img_path)

    # 缩略图
    thumbnail_pic = get_thumbnail(img_path)
    thumbnail_pic.show()

    # 绘制文字
    text_img = draw_text(img_path,"你好！",(0,0))
    text_img.show()

    # 图像增强
    #enhance(img_path)

    # 压缩图片
    #compress_image(img_path, img_path[:-4]+"_compressed" + ".jpg")
