import PIL ,PIL.Image
import glob
for fimg in glob.glob("*.png"):
    img = PIL.Image.open(fimg)
    img = img.convert("RGBA")
    datas = img.getdata()
    ndata = []
    diff = 50
    for px in datas:
        if ((px[0] > 15 - diff) & (px[0] < 15 + diff) &
                (px[1] > 191 - diff) & (px[1] < 191 + diff) &
                (px[2] > 33 - diff) & (px[2] < 33 + diff)):
            ndata.append((px[0], px[1], px[2], 0))
        else:
            ndata.append(px)

    img.putdata(ndata)
    img.save('../sprites/'+fimg)
    print(fimg)

