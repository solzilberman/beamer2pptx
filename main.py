import subprocess
import os 
import sys 
import shutil
from pptx import Presentation
from pptx.util import Inches
import glob

outdir="imgs"
fname="beamer.pdf"
cmd=f"pdftoppm {fname} {outdir}/slide -png -scale-to-x 1920 -scale-to-y 1080"
if os.path.exists(outdir):
    shutil.rmtree(outdir)
os.mkdir(outdir)
subprocess.run(cmd, shell=True)

PPTX_FNAME="test.pptx"
if os.path.exists(PPTX_FNAME):
    os.remove(PPTX_FNAME)
slide_pngs = glob.glob(f"{outdir}/*.png")
slide_pngs.sort()

prs = Presentation()
blank_slide_layout = prs.slide_layouts[6]

for slide_png in slide_pngs:
    slide = prs.slides.add_slide(blank_slide_layout)
    left = top = Inches(0)
    pic = slide.shapes.add_picture(slide_png, left, top, width=prs.slide_width, height=prs.slide_height)
prs.save(PPTX_FNAME)