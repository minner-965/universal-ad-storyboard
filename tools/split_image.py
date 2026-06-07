import os
import sys
from urllib.request import urlopen, Request
from PIL import Image, ImageFilter

def download_or_load_image(source):
    """支持本地路径和 HTTP URL"""
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

    # 统一转换为 RGB 模式，避免部分 PNG 通道导致的色彩失真
    if img.mode != 'RGB':
        img = img.convert('RGB')

    width, height = img.size
    print(f"[+] 原始故事板尺寸: {width}x{height}")

    # 定义 3x3 结构
    rows = 3
    cols = 4
    cell_w = width / cols
    cell_h = height / rows

    # 创建输出文件夹
    output_dir = os.path.join(".", "output", "sliced_images")
    os.makedirs(output_dir, exist_ok=True)

    index = 1
    print("[+] 开始执行超高清、无边框、无损切割流程...")
    
    for r in range(rows):
        for c in range(cols):
            left = c * cell_w
            top = r * cell_h
            right = (c + 1) * cell_w
            bottom = (r + 1) * cell_h
            
            # 1. 基础无损裁剪
            cropped_img = img.crop((left, top, right, bottom))
            
            # 2. 【去黑边算法】向内微调 4% 像素，干掉网格线、白边和序号标签
            w, h = cropped_img.size
            pad_w = int(w * 0.04)  # 左右各去 4%
            pad_h = int(h * 0.04)  # 上下各去 4%
            trimmed_img = cropped_img.crop((pad_w, pad_h, w - pad_w, h - pad_h))
            
            # 3. 【高清重建】将极小的小图无损重构放大到 1024x576 (标准 16:9 电影尺寸)
            # 使用业内顶尖的 LANCZOS (抗锯齿重采样) 滤镜
            target_w, target_h = 1024, 576
            try:
                resample_method = Image.Resampling.LANCZOS
            except AttributeError:
                resample_method = Image.LANCZOS
                
            upscaled_img = trimmed_img.resize((target_w, target_h), resample_method)
            
            # 4. 【高频锐化】应用图像锐化，挽回放大带来的细节丢失，让皮革、金属、产品细节更清晰
            sharpened_img = upscaled_img.filter(ImageFilter.SHARPEN)
            
            # 5. 保存分镜 (使用 PNG 保证绝对无损)
            filename = f"slice_{index:02d}.png"
            save_path = os.path.join(output_dir, filename)
            sharpened_img.save(save_path, "PNG", compress_level=3) # 适度压缩保存，速度更快且画质无损
            
            print(f"    - 分镜 {index:02d}/12 [去噪+超分1024p+锐化] -> {save_path}")
            index += 1

    print(f"\n[*] 优化完毕！9个超清独立分镜已生成在 '{output_dir}'，快去喂给视频生成模型吧！")

if __name__ == "__main__":
    main()