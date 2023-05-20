import json

from django.http import JsonResponse
from django.views.generic import UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from reforms.models import City


@method_decorator(csrf_exempt, name='dispatch')
class CityUpdateView(UpdateView):
    # TODO напишите здесь Ваш код
    model = City
    fields = ['name', 'description']

    def post(self, request, *args, **kwargs):
        city_data = json.loads(request.body)
        new_city, created = City.objects.update_or_create(
            name=city_data['name'],
            defaults={
                'description': city_data['description'],
            }
        )

        return JsonResponse({
            'id': new_city.id,
            'name': new_city.name,
            'description': new_city.description,
        }, safe=False)
