from __future__ import absolute_import, unicode_literals

import requests

from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from django.db import models

from modelcluster.fields import ParentalKey


from wagtail.core.models import Orderable, Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel
#from django.shortcuts import render

from wagtail.snippets.models import register_snippet

from wagtail.images.edit_handlers import ImageChooserPanel

from taggit.models import TaggedItemBase
from taggit.managers import TaggableManager



from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)

from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField

from modelcluster.models import ClusterableModel

class FormField(AbstractFormField):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='form_fields')


class HomePage(AbstractEmailForm):
    body = RichTextField(blank=True)
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)
    intro_support = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('body', classname="full"),
        FieldPanel('intro', classname="full"),
        FieldPanel('intro_support', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['number'] = 23;
        # Call the API to get numbers, current only use day
        response = requests.get("https://visitor.express/api/v1/health/")
        health = response.json()
        year = health['month']
        context['bookings_year'] = year['bookings']
        context['visitors_year'] = year['visitors']
        context['access_queries_year'] = year['access_queries']
        month = health['month']
        context['bookings_month'] = month['bookings']
        context['visitors_month'] = month['visitors']
        context['access_queries_month'] = month['access_queries']
        week = health['week']
        context['bookings_week'] = week['bookings']
        context['visitors_week'] = week['visitors']
        context['access_queries_week'] = week['access_queries']
        day = health['day']
        context['bookings_day'] = day['bookings']
        context['visitors_day'] = day['visitors']
        context['access_queries_day'] = day['access_queries']
        return context


class CaseStudySnippetTag(TaggedItemBase):
    content_object = ParentalKey('home.CaseStudySnippet', on_delete=models.CASCADE, related_name='tagged_items')

@register_snippet
class CaseStudySnippet(ClusterableModel):
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    active = models.BooleanField()
    order = models.IntegerField()

    tags = TaggableManager(through=CaseStudySnippetTag, blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('feed_image'),
        FieldPanel('body', classname='description'),
        FieldPanel('active'),
        FieldPanel('order'),
        FieldPanel('tags'),
    ]


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']


class AboutSnippetTag(TaggedItemBase):
    content_object = ParentalKey('home.AboutSnippet', on_delete=models.CASCADE, related_name='tagged_items')


@register_snippet
class AboutSnippet(ClusterableModel):
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    active = models.BooleanField()
    order = models.IntegerField()

    tags = TaggableManager(through=AboutSnippetTag, blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('feed_image'),
        FieldPanel('body', classname='description'),
        FieldPanel('active'),
        FieldPanel('order'),
        FieldPanel('tags'),
    ]


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']



class VisitorExpressSnippetTag(TaggedItemBase):
    content_object = ParentalKey('home.VisitorExpressSnippet', on_delete=models.CASCADE, related_name='tagged_items')

@register_snippet
class VisitorExpressSnippet(ClusterableModel):
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    active = models.BooleanField()
    order = models.IntegerField()

    tags = TaggableManager(through=VisitorExpressSnippetTag, blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('feed_image'),
        FieldPanel('body', classname='description'),
        FieldPanel('active'),
        FieldPanel('order'),
        FieldPanel('tags'),
    ]


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']


class Click2ParkSnippetTag(TaggedItemBase):
    content_object = ParentalKey('home.Click2ParkSnippet', on_delete=models.CASCADE, related_name='tagged_items')


@register_snippet
class Click2ParkSnippet(ClusterableModel):
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    active = models.BooleanField()
    order = models.IntegerField()

    tags = TaggableManager(through=Click2ParkSnippetTag, blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('feed_image'),
        FieldPanel('body', classname='description'),
        FieldPanel('active'),
        FieldPanel('order'),
        FieldPanel('tags'),
    ]


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']

class Journey2ShareSnippetTag(TaggedItemBase):
    content_object = ParentalKey('home.Journey2ShareSnippet', on_delete=models.CASCADE, related_name='tagged_items')


@register_snippet
class Journey2ShareSnippet(ClusterableModel):
    title = models.CharField(max_length=255, blank=True)
    url = models.URLField(null=True, blank=True)
    text = models.CharField(max_length=255)
    body = RichTextField(blank=True)
    active = models.BooleanField()
    order = models.IntegerField()

    tags = TaggableManager(through=Journey2ShareSnippetTag, blank=True)

    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('title'),
        ImageChooserPanel('feed_image'),
        FieldPanel('body', classname='description'),
        FieldPanel('active'),
        FieldPanel('order'),
        FieldPanel('tags'),
    ]


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']



class TestPage(Page):
    body = RichTextField(blank=True)
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)



# not needed
class CarouselItem(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    caption = models.CharField(max_length=255, blank=True)
    visitor_express_page = ParentalKey(VisitorExpressSnippet, related_name='carousel_links',null=True,blank=True)
    about_page = ParentalKey(AboutSnippet, related_name='carousel_links',null=True,blank=True)
    click2park_page = ParentalKey(Click2ParkSnippet, related_name='carousel_links',null=True,blank=True)
    journey2share_page = ParentalKey(Journey2ShareSnippet, related_name='carousel_links',null=True,blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

    def __str__(self):
        return self.caption
