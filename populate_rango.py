import os
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'tango_with_django_project.settings'
)

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
         'url':'http://docs.python.org/3/tutorial/',
         'views': 27},
        {'title':'How to Think like a Computer Scientist',
         'url':'http://www.greenteapress.com/thinkpython/',
         'views': 34},
        {'title':'Learn Python in 10 Minutes',
         'url':'http://www.korokithakis.net/tutorials/python/',
         'views': 16}
    ]

    django_pages = [
        {'title':'Official Django Tutorial',
         'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 42},
        {'title':'Django Rocks',
         'url':'http://www.djangorocks.com/',
         'views': 19},
        {'title':'How to Tango with Django',
         'url':'http://www.tangowithdjango.com/',
         'views': 4}
    ]

    other_pages = [
        {'title':'Bottle',
         'url':'http://bottlepy.org/docs/dev/',
         'views': 7},
        {'title':'Flask',
         'url':'http://flask.pocoo.org',
         'views': 14}
    ]

    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }

    MAX_VIEWS = 301

    for category, category_data in cats.items():
        c = add_category(category, category_data['views'], category_data['likes'])
        for page in category_data['pages']:
            add_page(c, page['title'], page['url'],page['views'])
    
    for category in Category.objects.all():
        for page in Page.objects.filter(category=category):
            print(f'- {category}: {page}')

def add_page(category, title, url, views=0):
    page = Page.objects.get_or_create(category=category, title=title)[0]
    page.url = url
    page.views = views
    page.save()
    return page

def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name)[0]
    category.views = views
    category.likes = likes
    category.save()
    return category

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
