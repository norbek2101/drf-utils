from django.db import models


class Util(models.Model):
    name = models.CharField("Project name", max_length=200)
    picture = models.ImageField("Project picture", upload_to="media")
    icon = models.CharField("Icon name", max_length=20)
    author = models.CharField("Project author", max_length=50)
    is_organization = models.BooleanField(default=False)
    email = models.EmailField()
    phone_number = models.CharField("Phone number", max_length=20)
    html_content = models.TextField()
    description = models.CharField("Description", max_length=50)
    api_link = models.URLField()

    class Meta:
        verbose_name = "Util"
        verbose_name_plural = "Utils"

    def __str__(self):
        return self.name
