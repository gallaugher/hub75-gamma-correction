# Hub75-64x32-hack.py
import board, displayio, time, gc, random, math, rgbmatrix, framebufferio
from adafruit_display_text.bitmap_label import Label
from adafruit_bitmap_font import bitmap_font
from smooth_scroller import SmoothScroller

# --- Display Setup ---
displayio.release_displays()

# === Setup for Pico ===
# Setup rgbmatrix display (change pins to match your wiring)
matrix = rgbmatrix.RGBMatrix(
   width=64, # Change width & height if you have an LED matrix with different dimensions
   height=32,
   bit_depth=6,
   rgb_pins=[ # Preserve GP4 & GP5 for standard STEMMA-QT
       board.GP2,   # R1
       board.GP3,   # G1
       board.GP6,   # B1
       board.GP7,   # R2
       board.GP8,   # G2
       board.GP9    # B2
   ],
   addr_pins=[
       board.GP10,  # A
       board.GP16,  # B
       board.GP18,  # C
       board.GP20   # D
   ],
   clock_pin=board.GP11,
   latch_pin=board.GP12,
   output_enable_pin=board.GP13,
   tile=1,
   serpentine=False,
   doublebuffer=True,
)

display = framebufferio.FramebufferDisplay(matrix)
# === end of pico setup === #
group = displayio.Group() # creates an empy group
display.root_group = group



# read in image from board
bitmap = displayio.OnDiskBitmap("/images/blinka.bmp") # read in image
tilegrid = displayio.TileGrid(bitmap, pixel_shader=bitmap.pixel_shader)

group.append(tilegrid)

label_font = bitmap_font.load_font("/fonts/helvB08.bdf")

text_label = Label(
    font=label_font,
    text="Gamma\nCorrect",
    background_tight=True,
    anchor_point=(0,0),
    anchored_position=(display.width//2-7, 0),
    line_spacing=0.7
)
group.append(text_label)

print("Running!")

while True:
    pass