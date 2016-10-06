from django.views.generic import TemplateView

from make_files import make_js_paths, make_image_paths


class HeavyView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HeavyView, self).get_context_data(**kwargs)
        context['js_paths'] = list(make_js_paths(root=''))
        context['image_paths'] = list(make_image_paths(root=''))
        return context
