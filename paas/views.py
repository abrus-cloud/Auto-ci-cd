from django.views.generic import TemplateView
from .forms import HomeForm
from django.shortcuts import render


class Home(TemplateView):
    template_name = 'paas/home.html'

    def get(self, request):
        form = HomeForm()
        args = {'form': form}
        return render(request, self.template_name, args)

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            moz = form.cleaned_data['moz']
            args = {'moz': moz,
                    'form': form,
                    }
        return render(request, self.template_name, args)


