from PIL import Image, ImageDraw
from PIL import ImageFont
import json

data=json.load(open("pokemon survey results/final results.json"))

#image1 = image.open('types.png')

for qustion in data:
    im = Image.open("pokemon survey results/template.png")
    draw = ImageDraw.Draw(im)   
    #qustion="Favourite Water Type"
    #draw.rectangle(((0,0),(100,100)), fill="#ffffff", outline="#000000")

    for rank,value in data[qustion].items():
        print(rank,value)
        try:
            icon = Image.open(f'pokemon survey results/images/{value.lower()}.png', 'r')
            iconW,iconH = icon.size
            icon=icon.crop((0,0,iconW-(iconW%20),21*(iconW//20)))
        except:
            icon=None
            print("No Image")

        #draw.rectangle(((x,y),(x+width,cany)), fill=colours[qustion][value], outline="#000000")
        if rank=="1st":
            icon=icon.resize((int(icon.size[0]*(587/icon.size[1])), 587 ))
            im.paste(icon, ((im.size[0]//2)-(icon.size[0]//2),20), mask=icon)
        elif rank=="2nd":
            icon=icon.resize((int(icon.size[0]*(473/icon.size[1])), 473 ))
            im.paste(icon, ((im.size[0]//2)-(icon.size[0]),610), mask=icon)
        elif rank=="3rd":
            icon=icon.resize((int(icon.size[0]*(473/icon.size[1])), 473 ))
            im.paste(icon, ((im.size[0])-(icon.size[0]),610), mask=icon)
        else:
            if len(data[qustion])>11:
                fontsize=75
                font = ImageFont.truetype("arial.ttf", fontsize, encoding="unic")

                index=(list(data[qustion]).index(rank)-3)%((len(data[qustion])-3)/2)
                movex=((list(data[qustion]).index(rank)-3)//((len(data[qustion])-3)/2))
                x=90+((im.size[0]//2)*movex)
                y=1189+(index*(fontsize+10))
                draw.text((x, y),f"{rank:>4} - {value}",(255,255,255),font=font,stroke_width=5, stroke_fill="#000000")
                print(index)
            else:
                fontsize=85
                font = ImageFont.truetype("arial.ttf", fontsize, encoding="unic")
                index=list(data[qustion]).index(rank)-3

                biggest_word=int(max([len(f"10th - {nx}") for nx in data[qustion].values()])*0.75)

                movex=(fontsize*biggest_word)
                x=(int(im.size[0]*0.75)-int(movex//2))
                y=1189+(index*(fontsize+10))
                draw.text((x, y),f"{rank:>4} - {value}",(255,255,255),font=font,stroke_width=5, stroke_fill="#000000")


    im.save(f'pokemon survey results/charts/{qustion}.png')