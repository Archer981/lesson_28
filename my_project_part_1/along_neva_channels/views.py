from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from along_neva_channels.models import Tour


# TODO Здесь необходимо реализовать CBV в соответствии со спецификацией
class TourListView(ListView):
    model = Tour

    def get(self, request, **kwargs):
        super().get(request, **kwargs)
        result = []
        for i in self.object_list:
            result.append({
                'id': i.id,
                'name': i.name,
                'starts_at': i.starts_at if i.starts_at else '',
                'ends_at': i.ends_at if i.ends_at else '',
                'points': list({'name': point.name} for point in i.points.all())
            })
            print(result)
        return JsonResponse(result, safe=False)


class TourDetailView(DetailView):
    model = Tour

    def get(self, request, **kwargs):
        super().get(request, **kwargs)
        tour_data = self.get_object()
        return JsonResponse({
            'id': tour_data.id,
            'name': tour_data.name,
            'starts_at': tour_data.starts_at,
            'ends_at': tour_data.ends_at,
            'points': list(tour_data.points.all().values_list('name', flat=True))
            }, safe=False)
