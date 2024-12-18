from django.db import models


# Create your models here.
class HSRCharacter(models.Model):
    name = models.CharField(max_length=40, blank=False)
    description = models.TextField(blank=True)

    picture = models.ImageField(upload_to='character_pics', blank=True)

    debut_date = models.DateField(blank=True)

    basic_attack = models.TextField(blank=True)
    skill = models.TextField(blank=True)
    ultimate = models.TextField(blank=True)
    talent = models.TextField(blank=True)
    technique = models.TextField(blank=True)

    trace_1 = models.TextField(blank=True)
    trace_2 = models.TextField(blank=True)
    trace_3 = models.TextField(blank=True)

    eidolon_1 = models.TextField(blank=True)
    eidolon_2 = models.TextField(blank=True)
    eidolon_3 = models.TextField(blank=True)
    eidolon_4 = models.TextField(blank=True)
    eidolon_5 = models.TextField(blank=True)
    eidolon_6 = models.TextField(blank=True)

    ElementType = [
        ("PHYSICAL", "Physical"),
        ("FIRE", "Fire"),
        ("ICE", "Ice"),
        ("LIGHTNING", "Lightning"),
        ("WIND", "Wind"),
        ("QUANTUM", "Quantum"),
        ("IMAGINARY", "Imaginary"),
    ]
    element_type = models.CharField(max_length=20, choices=ElementType, blank=True)

    PathType = [
        ("ABUNDANCE", "Abundance"),
        ("DESTRUCTION", "Destruction"),
        ("ERUDITION", "Erudition"),
        ("HARMONY", "Harmony"),
        ("HUNT", "Hunt"),
        ("NIHILITY", "Nihility"),
        ("PRESERVATION", "Preservation"),
    ]
    path_type = models.CharField(max_length=20, choices=PathType, blank=True)

    StarLevel = [
        (3, "Three"),
        (4, "Four"),
    ]
    star_level = models.IntegerField(choices=StarLevel, blank=True)
