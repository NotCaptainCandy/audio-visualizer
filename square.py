from PIL import Image, ImageDraw, ImageFilter
import sys

base = Image.new('RGB', (1000, 1000), color='black')

def draw(vals, column):
    sqr = ImageDraw.Draw(base)
    sqr.rectangle([(column*200,1000),(column*200+200, 900)], fill=f'hsl({280*(1-vals[0])}, 100%, {70*vals[0]}%)', outline=None, width=0)
    sqr.rectangle([(column*200,900),(column*200+200, 800)], fill=f'hsl({280*(1-vals[1])}, 100%, {70*vals[1]}%)', outline=None, width=0)
    sqr.rectangle([(column*200,800),(column*200+200, 700)], fill=f'hsl({280*(1-vals[2])}, 100%, {70*vals[2]}%)', outline=None, width=0)
    sqr.rectangle([(column*200,700),(column*200+200, 600)], fill=f'hsl({280*(1-vals[3])}, 100%, {70*vals[3]}%)', outline=None, width=0)
    sqr.rectangle([(column*200,600),(column*200+200, 500)], fill=f'hsl({280*(1-vals[4])}, 100%, {70*vals[4]}%)', outline=None, width=0)
    sqr.rectangle([(column*200,500),(column*200+200, 400)], fill=f'hsl({280*(1-vals[5])}, 100%, {70*vals[5]}%)', outline=None, width=0)
    sqr.rectangle([(column*200,400),(column*200+200, 300)], fill=f'hsl({280*(1-vals[6])}, 100%, {70*vals[6]}%)', outline=None, width=0)
    sqr.rectangle([(column*200,300),(column*200+200, 200)], fill=f'hsl({280*(1-vals[7])}, 100%, {70*vals[7]}%)', outline=None, width=0)
    sqr.rectangle([(column*200,200),(column*200+200, 100)], fill=f'hsl({280*(1-vals[8])}, 100%, {70*vals[8]}%)', outline=None, width=0)
    sqr.rectangle([(column*200,100),(column*200+200, 0)], fill=f'hsl({280*(1-vals[9])}, 100%, {70*vals[9]}%)', outline=None, width=0)

def save(filename):
    guass = base.filter(ImageFilter.GaussianBlur(151))
    guass.save(f"{filename}.png")