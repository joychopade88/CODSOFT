from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import warnings

warnings.filterwarnings("ignore")

def caption_image(image_path):
    try:
        # Initialize the processor and model directly to avoid pipeline version errors
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        
        # Open image and convert to RGB (crucial for .webp files to avoid errors)
        image = Image.open(image_path).convert('RGB')
        
        # Process the image and generate the caption
        inputs = processor(image, return_tensors="pt")
        out = model.generate(**inputs)
        caption = processor.decode(out[0], skip_special_tokens=True)
        
        return caption
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    path = input("Enter image file path (e.g., photo.jpg): ")
    print("Loading model and generating caption (this may take a moment)...")
    print("Caption:", caption_image(path))