from django import template

register = template.Library()


@register.simple_tag()
def truncate_docs(doc_name):
    doc_name = doc_name.split('/')
    try:
        return doc_name[1]
    except:
        return 'file'
