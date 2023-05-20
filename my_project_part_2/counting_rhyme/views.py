from django.http import JsonResponse
from django.views import View

from counting_rhyme.models import User, City


# TODO внесите необходимые изменения в код ниже
class CountView(View):

    def get(self, request):
        users_count = User.objects.count()
        cities_count = City.objects.count()
        return JsonResponse({
            "cities": cities_count,
            "users": users_count,
        })
