from django.contrib import admin

from .models import Education
from .models import Experience
from .models import Language
from .models import Skill
from .models import Extracurricular_and_hobby

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass

@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass

@admin.register(Extracurricular_and_hobby)
class ExtracurricularAdmin(admin.ModelAdmin):
    pass
