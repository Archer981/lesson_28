import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from forgotten.models import Review


# TODO здесь необходимо реализовать CBV в соответствии с заданием
@method_decorator(csrf_exempt, name="dispatch")
class ReviewUpdateView(UpdateView):
    model = Review
    fields = ['author', 'tour', 'content', 'rate', 'published_at', 'is_published']

    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        review_data = json.loads(request.body)
        self.object.content = review_data.get('content', self.object.content)
        self.object.rate = review_data.get('rate', self.object.rate)
        self.object.save()
        return JsonResponse({
            'id': self.object.id,
            'author': self.object.author,
            'tour': self.object.tour_id,
            'content': self.object.content,
            'rate': self.object.rate,
            'published_at': self.object.published_at,
            'is_published': self.object.is_published,
        }, safe=False)


