from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('test', '0010_user_bio'),
    ]

    operations = [
        migrations.RunSQL(
            "SELECT 1;",  # ローカルでは何もしない
            migrations.RunSQL.noop
        ),
    ]