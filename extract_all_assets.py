import os
import io
import PyPDF2
from PIL import Image

pdf_path = r"C:\Users\SURFACE LAPTOP\Downloads\Regan Peter Costa  CV Nurisng (1).pdf"
out_dir = r"C:\Users\SURFACE LAPTOP\.gemini\antigravity\scratch\regan_costa_nursing_cv\public\credentials"
os.makedirs(out_dir, exist_ok=True)

reader = PyPDF2.PdfReader(pdf_path)

# Map page index to clean descriptive filenames and orientation fix
# We can check each page's image
images_info = [
    # (page_num_1indexed, filename, title, category, rotate_degrees)
    (1, "candidate_photo.jpg", "Official Portrait Photo", "Identity", 0),
    (3, "candidate_signature.jpg", "Official Signature", "Identity", 0),
    (4, "bnc_diploma_certificate.jpg", "Diploma in Nursing Science & Midwifery Certificate", "Nursing License & Education", 0),
    (5, "green_life_testimonial.jpg", "Green Life Hospital Nursing Institute Testimonial", "Nursing Education", 270), # page 5 was sideways in screenshot
    (6, "hsc_certificate.jpg", "Higher Secondary Certificate (HSC)", "Academic Education", 270), # page 6 was sideways
    (7, "ssc_certificate.jpg", "Secondary School Certificate (SSC)", "Academic Education", 270), # page 7 was sideways
    (8, "bnmc_smart_card_license.jpg", "Bangladesh Nursing & Midwifery Council (BNMC) Smart Card License", "Nursing License & Education", 0),
    (9, "square_hospital_experience_certificate.jpg", "Square Hospitals Ltd. Recommendation & Experience Certificate", "Clinical Experience", 0),
    (10, "bls_provider_certificate.jpg", "Basic Life Support (BLS) Provider Certificate", "Certifications", 0),
    (11, "national_id_card.jpg", "Bangladesh National Identity Card (NID)", "Identity", 0)
]

for page_idx_1, filename, title, cat, rot in images_info:
    page = reader.pages[page_idx_1 - 1]
    if len(page.images) > 0:
        img_data = page.images[0].data
        img = Image.open(io.BytesIO(img_data))
        
        # Check if rotation is needed
        if rot != 0:
            # Let's check dimensions before rotating
            w, h = img.size
            if w > h and rot in [90, 270]:
                img = img.rotate(rot, expand=True)
                print(f"Rotated {filename} by {rot} deg")
        
        target_file = os.path.join(out_dir, filename)
        img.save(target_file, quality=95)
        print(f"Saved: {filename} ({img.size[0]}x{img.size[1]}) - {title}")

print("\nAll certificates and licenses extracted successfully!")
