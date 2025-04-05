from PIL import Image, ImageDraw, ImageFont
import emoji


img = Image.new('RGB', (500, 500), color=(255, 255, 255))


draw = ImageDraw.Draw(img)


font = ImageFont.load_default()

# Get the heart emoji text
heart_emoji = emoji.emojize(':red_heart:')

# Add the heart emoji to the image
draw.text((150, 200), heart_emoji, font=font, fill=(255, 0, 0))


img.show()
