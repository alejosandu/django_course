import os
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
django.setup()

from first_app.models import Topic, WebPage, AccessRecord

topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    """function to populate the database"""
    fake = Faker()
    for entry in range(N):
        # get the topic for the entry
        topic = add_topic()

        # create all related data
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.name()

        webpage = WebPage.objects.get_or_create(
            topic=topic, url=fake_url, name=fake_name,
        )[0]

        access_record = AccessRecord.objects.get_or_create(
            name=webpage, date=fake_date,
        )[0]


if __name__ == '__main__':
    print('populating')
    populate(20)
    print('population completed')
