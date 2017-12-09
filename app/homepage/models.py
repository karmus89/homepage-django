from django.db import models
from django.utils.text import slugify
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class NavigablePage(models.Model):
    """
    A base model for each page with an associated link in the navigation bar.
    """
    class Meta:
        ordering = ('order',)

    order = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title or ''


class TextPage(NavigablePage):
    """
    A model for a single page with Markdown content.
    """

    content = MarkdownxField()

    @property
    def content_md(self):
        return markdownify(self.content)