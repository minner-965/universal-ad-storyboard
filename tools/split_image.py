import os
import sys
from urllib.request import urlopen, Request
from PIL import Image

def download_or_load_image(source):
    """支持本地路径和 HTTP URL (使用标准 urllib 避免依赖)"""
    if source.startswith(('http://', 'https://')):
        print(f"[+] 正在从网络下载故事板大图: {source}")
        req = Request(source, headers={'User-Agent': 'Mozilla/5.0'})
        with urlopen(req, timeout=15) as response:
            return Image.open(response)
    else:
        if not os.path.exists(source):
            raise FileNotFoundError(f"[-] 本地文件未找到: {source}")
        print(f"[+] 正在加载本地故事板大图: {source}")
        return Image.open(source)

def main():
    if len(sys.argv) < 2:
        print("Usage: python split_image.py <image_url_or_local_path>")
        sys.exit(1)

    source = sys.argv[1]
    
    try:
        img = download_or_load_image(source)
    except Exception as e:
        print(f"[-] 图片加载失败: {e}")
        sys.exit(1)

    width, height = img.size
    print(f"[+] 大图尺寸: {width}x{height}")

    # 定义 3x5 结构
    rows = 3
    cols = 5
    cell_w = width / cols
    cell_h = height / rows

    # 创建输出文件夹
    output_dir = os.path.join(".", "output", "sliced_images")
    os.makedirs(output_dir, exist_ok=True)

    index = 1
    print("[+] 开始自动切割分镜...")
    
    for r in range(rows):
        for c in range(cols):
            left = c * cell_w
            top = r * cell_h
            right = (c + 1) * cell_w
            bottom = (r + 1) * cell_h
            
            # 无损裁剪并高清放大以提升视频剪辑质量
            cropped_img = img.crop((left, top, right, bottom))
            target_width = 1080
            target_height = int(target_width * (cell_h / cell_w))
            
            # 使用 LANCZOS 算法进行高质量超分放大
            try:
                resample_method = Image.Resampling.LANCZOS
            except AttributeError:
                resample_method = Image.LANCZOS # 兼容旧版 Pillow
                
            high_res_img = cropped_img.resize((target_width, target_height), resample_method)
            
            filename = f"slice_{index:02d}.png"
            save_path = os.path.join(output_dir, filename)
            high_res_img.save(save_path, "PNG", optimize=False)
            print(f"    - 已保存高清分镜 {index:02d}/15 -> {save_path}")
            index += 1

    print(f"\n[*] 恭喜！15个独立分镜已全部切片并高清放大完成！请在目录 '{output_dir}' 中查看。")

if __name__ == "__main__":
    main()
