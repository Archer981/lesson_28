from django.http import JsonResponse
from django.views.generic import DetailView, ListView

from discounts.models import Discount


# TODO здесь необходимо реализовать СBV которые
# TODO бы возвращали данные в соответствии со спецификацией
class DiscountListView(ListView):
    model = Discount

    def get(self, request, **kwargs):
        super().get(request, **kwargs)
        result = []
        for i in self.object_list:
            result.append({
                'id': i.id,
                'tour': i.tour_id,
                'category': i.category,
                'discount': i.discount,
                'code': i.code,
                'starts_at': i.starts_at,
                'ends_at': i.ends_at,
            })
        return JsonResponse(result, safe=False)


class DiscountDetailView(DetailView):
    model = Discount

    def get(self, request, **kwargs):
        data = self.get_object()
        return JsonResponse({
            'id': data.id,
            'tour': data.tour_id,
            'category': data.category,
            'discount': data.discount,
            'code': data.code,
            'starts_at': data.starts_at,
            'ends_at': data.ends_at,
        }, safe=False)
