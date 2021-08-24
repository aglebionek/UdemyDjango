import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_project.settings')

import django
django.setup()

import random
from test_app.models import AccessRecord, Topic, Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for _ in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage_entry = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        account_entry = AccessRecord.objects.get_or_create(name=webpage_entry, date=fake_date)[0]

if __name__ == "__main__":
    print("populating model")
    populate(20)
    print("populating complete")