from django.db import models
from django.core.validators import FileExtensionValidator
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = ProcessedImageField(
        upload_to='products/',
        processors=[ResizeToFill(300, 300)],
        options={'quality': 90},
        default='products/default.png',
        blank=True,
        null=True,
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])]
    )
    description = models.TextField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name