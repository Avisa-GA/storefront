# Generated by Django 4.1.3 on 2022-12-06 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL("""
            INSERT INTO store_collection(title) 
            VALUES ('test collection');
        """, """
            DELETE FROM store_collection WHERE title = 'test collection';
        """)
    ]
