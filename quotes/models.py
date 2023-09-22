from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Author(models.Model):
    fullname = models.CharField(max_length=255, null=False)
    born_date = models.DateField()
    born_location = models.CharField(max_length=255)
    biography = models.TextField()
    user = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING, default=1)
    slug = models.SlugField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        return super().save(*args, **kwargs)


class Tag(models.Model):
    tag = models.CharField(max_length=128, null=False, unique=True)
    user = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING, default=1)
    slug = models.SlugField(unique=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ("tag",)

    def __str__(self):
        return f"{self.tag}"

    def get_absolute_url(self):
        return reverse("tag_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.tag)
        return super().save(*args, **kwargs)


class Quote(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
    quote = models.TextField()
    user = models.ForeignKey("auth.User", on_delete=models.DO_NOTHING, default=1)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.quote[:56] + "..."
