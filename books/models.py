from django.db import models
import uuid
from services.r2_storage import R2Storage


def cover_image_upload_path(instance, filename):
    # Store as: cover_images/cover_<uuid4>_<original_filename>
    unique_id = uuid.uuid4()
    return f"cover_images/cover_{unique_id}_{filename}"


class Book(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    pages = models.IntegerField(blank=True, null=True)
    cover_image = models.ImageField(
        upload_to=cover_image_upload_path,
        blank=True,
        null=True,
        max_length=500
    )
    pdf_key = models.CharField(max_length=500, blank=True, null=True)  # Store the R2 object key
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title or "Untitled Book"

    @property
    def download_url(self):
        if self.pdf_key:
            r2 = R2Storage()  # Optionally pass bucket_name if needed
            return r2.get_view_url(self.pdf_key, expires_in=3600)
        return None

    @property
    def formatted_date(self):
        if self.published_date:
            return self.published_date.strftime('%B %d, %Y')
        return ""