import os
from PIL import Image, ImageOps

BASE = r"D:\IA\MCP\quem-canta-tv-app"
ASSETS = os.path.join(BASE, "assets")
RES = os.path.join(BASE, "app", "src", "main", "res")

os.makedirs(ASSETS, exist_ok=True)

logo_path = os.path.join(ASSETS, "logo.png")
favicon_path = os.path.join(ASSETS, "favicon.png")

logo_img = Image.open(logo_path).convert("RGBA")
fav_img = Image.open(favicon_path).convert("RGBA")

# 1. TV Banner: 320x180
banner_w, banner_h = 320, 180
banner = Image.new("RGBA", (banner_w, banner_h), (8, 13, 26, 255)) # Dark #080d1a background

# Fit logo inside banner (e.g. max 260x130)
logo_resized = logo_img.copy()
logo_resized.thumbnail((260, 130), Image.Resampling.LANCZOS)
ox = (banner_w - logo_resized.width) // 2
oy = (banner_h - logo_resized.height) // 2
banner.paste(logo_resized, (ox, oy), logo_resized)

drawable_dir = os.path.join(RES, "drawable")
os.makedirs(drawable_dir, exist_ok=True)
banner.save(os.path.join(drawable_dir, "banner.png"))
print("Saved banner.png 320x180")

# 2. Launcher Icons in mipmaps
sizes = {
    "mipmap-mdpi": 48,
    "mipmap-hdpi": 72,
    "mipmap-xhdpi": 96,
    "mipmap-xxhdpi": 144,
    "mipmap-xxxhdpi": 192
}

for folder, sz in sizes.items():
    fdir = os.path.join(RES, folder)
    os.makedirs(fdir, exist_ok=True)
    icon = Image.new("RGBA", (sz, sz), (8, 13, 26, 255))
    
    # Rounded mask or squircle
    fav_resized = fav_img.copy()
    fav_resized.thumbnail((int(sz * 0.82), int(sz * 0.82)), Image.Resampling.LANCZOS)
    fox = (sz - fav_resized.width) // 2
    foy = (sz - fav_resized.height) // 2
    icon.paste(fav_resized, (fox, foy), fav_resized)
    icon.save(os.path.join(fdir, "ic_launcher.png"))
    print(f"Saved {folder}/ic_launcher.png ({sz}x{sz})")

print("All visual assets prepared successfully!")
