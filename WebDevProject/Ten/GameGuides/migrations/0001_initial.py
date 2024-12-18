# Generated by Django 5.1.3 on 2024-11-23 00:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HSRCharacter",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=40)),
                ("description", models.TextField(blank=True)),
                ("picture", models.ImageField(blank=True, upload_to="character_pics")),
                ("debut_date", models.DateField(blank=True)),
                ("basic_attack", models.TextField(blank=True)),
                ("skill", models.TextField(blank=True)),
                ("ultimate", models.TextField(blank=True)),
                ("talent", models.TextField(blank=True)),
                ("technique", models.TextField(blank=True)),
                ("trace_1", models.TextField(blank=True)),
                ("trace_2", models.TextField(blank=True)),
                ("trace_3", models.TextField(blank=True)),
                ("eidolon_1", models.TextField(blank=True)),
                ("eidolon_2", models.TextField(blank=True)),
                ("eidolon_3", models.TextField(blank=True)),
                ("eidolon_4", models.TextField(blank=True)),
                ("eidolon_5", models.TextField(blank=True)),
                ("eidolon_6", models.TextField(blank=True)),
                (
                    "element_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("PHYSICAL", "Physical"),
                            ("FIRE", "Fire"),
                            ("ICE", "Ice"),
                            ("LIGHTNING", "Lightning"),
                            ("WIND", "Wind"),
                            ("QUANTUM", "Quantum"),
                            ("IMAGINARY", "Imaginary"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "path_type",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("ABUNDANCE", "Abundance"),
                            ("DESTRUCTION", "Destruction"),
                            ("ERUDITION", "Erudition"),
                            ("HARMONY", "Harmony"),
                            ("HUNT", "Hunt"),
                            ("NIHILITY", "Nihility"),
                            ("PRESERVATION", "Preservation"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "star_level",
                    models.IntegerField(
                        blank=True, choices=[(3, "Three"), (4, "Four")]
                    ),
                ),
            ],
        ),
    ]