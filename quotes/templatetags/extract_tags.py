from django import template

register = template.Library()


def tags(quote_tags):
    return [tag for tag in quote_tags.all()]


register.filter("tags", tags)
