# Erzeugt WebP-Versionen aller Fotos: images/photography/web (max. 2000px) und images/photography/thumb (max. 600px).
# Originale bleiben unverändert. Aufruf im Repo-Ordner: python3 tools/optimize-images.py  (benötigt Pillow)
import sys, os
from PIL import Image, ImageOps
from concurrent.futures import ProcessPoolExecutor
SRC="images/photography"
def conv(name):
    base=os.path.splitext(name)[0]
    im=Image.open(os.path.join(SRC,name)); icc=im.info.get("icc_profile")
    im=ImageOps.exif_transpose(im)
    if im.mode not in ("RGB","RGBA"): im=im.convert("RGB")
    out=[]
    for d,size,q in (("web",2000,82),("thumb",600,78)):
        os.makedirs(os.path.join(SRC,d),exist_ok=True)
        c=im.copy(); c.thumbnail((size,size),Image.LANCZOS)
        p=os.path.join(SRC,d,base+".webp")
        kw=dict(quality=q,method=6)
        if icc: kw["icc_profile"]=icc
        c.save(p,"WEBP",**kw); out.append(os.path.getsize(p))
    return name,im.size,out
if __name__=="__main__":
    # Pro Bildname eine Quelle: JPG/PNG vor WebP; schon erzeugte Versionen werden übersprungen
    # (mit --all alles neu erzeugen).
    pref={".jpg":0,".jpeg":0,".png":1,".webp":2}
    src={}
    for f in sorted(os.listdir(SRC)):
        b,e=os.path.splitext(f)
        if e.lower() in pref and (b not in src or pref[e.lower()]<pref[os.path.splitext(src[b])[1].lower()]): src[b]=f
    redo="--all" in sys.argv
    files=[f for b,f in sorted(src.items()) if redo or not all(
        os.path.exists(os.path.join(SRC,d,b+".webp")) and os.path.getmtime(os.path.join(SRC,d,b+".webp"))>=os.path.getmtime(os.path.join(SRC,f))
        for d in ("web","thumb"))]
    with ProcessPoolExecutor() as ex:
        for r in ex.map(conv,files): print(*r)
