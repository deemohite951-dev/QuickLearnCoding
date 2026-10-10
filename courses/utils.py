from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile


def generate_certificate_image(certificate):
    width, height = 1200, 850
    image = Image.new("RGB", (width, height), color="#FAF9F6")
    draw = ImageDraw.Draw(image)

    # Double Border
    draw.rectangle([(30, 30), (width - 30, height - 30)], outline="#0D6EFD", width=6)
    draw.rectangle([(45, 45), (width - 45, height - 45)], outline="#D4AF37", width=2)

    try:
        title_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 46)
        name_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 52)
        body_font = ImageFont.truetype("DejaVuSans.ttf", 26)
        small_font = ImageFont.truetype("DejaVuSans.ttf", 18)
    except IOError:
        title_font = name_font = body_font = small_font = ImageFont.load_default()

    # Title & Body
    draw.text((width // 2, 130), "CERTIFICATE OF COMPLETION", fill="#0D6EFD", anchor="mm", font=title_font)
    draw.text((width // 2, 220), "This is proudly presented to", fill="#6C757D", anchor="mm", font=body_font)

    student_name = certificate.user.get_full_name() or certificate.user.username
    draw.text((width // 2, 310), student_name, fill="#212529", anchor="mm", font=name_font)

    draw.text((width // 2, 400), "for successfully completing the 30-day intensive roadmap:", fill="#6C757D", anchor="mm", font=body_font)
    draw.text((width // 2, 470), f'"{certificate.course.title}"', fill="#0D6EFD", anchor="mm", font=title_font)

    # Footer Metadata
    date_str = certificate.issued_at.strftime("%B %d, %Y")
    draw.text((120, 680), f"Issue Date: {date_str}", fill="#495057", anchor="lm", font=small_font)
    draw.text((120, 715), f"Certificate ID: {certificate.certificate_code}", fill="#495057", anchor="lm", font=small_font)

    draw.text((width - 120, 680), "Learn in 30 Days", fill="#212529", anchor="rm", font=body_font)
    draw.text((width - 120, 715), "Verified Online Course", fill="#6C757D", anchor="rm", font=small_font)

    # Save PNG buffer to ImageField
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    filename = f"{certificate.certificate_code}.png"
    certificate.certificate_image.save(filename, ContentFile(buffer.getvalue()), save=True)