from django.views.generic import TemplateView

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'My About Page', 
            'body': 'Once upon a time ...',
        }

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'My Home Page', 
            'body': 'This page is boring ...',
        }

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        return {
            'title': 'This is the Index Page!', 
            'body': 'I am Index!',
        }