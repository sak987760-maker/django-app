from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('test', '0010_user_bio'),
    ]

    operations = [
        migrations.RunSQL(
            "ALTER TABLE test_ternal DROP COLUMN IF EXISTS bio;",
            migrations.RunSQL.noop
        ),
    ]