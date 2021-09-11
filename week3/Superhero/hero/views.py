from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class HulkView(TemplateView):
    template_name = 'hulk.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hulk',
            'body': 'My name is Bruce Banner',
            'image': '/static/images/hulk.jpg'
        }


class IronManView(TemplateView):
    template_name = "iron_man.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'Iron Man',
            'body': 'My name is Tony Stark, but I am Iron Man',
            'image': '/static/images/ironman.jpg'
        }


class BlackWidow(TemplateView):
    template_name = 'black_widow.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Black Widow',
            'body': 'My name is Natasha Romanova',
            'image': '/static/images/blackwidow.jpg'
        }