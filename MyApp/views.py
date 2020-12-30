from django.contrib import messages

from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, TemplateView
from MyApp.forms import CommentForm
from MyApp.models import Comments, Links, LinksThemes


class CommentsView(ListView):
    model = Comments
    queryset = Comments.objects.order_by('-date')[:8]
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        return context

class FishView(TemplateView):
    template_name = 'MyApp/fishpage.html'


class LinksView(ListView):
    model = Links
    queryset = Links.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['themes'] = LinksThemes.objects.all()
        return context
   


class AddCommentView(CreateView):
    model = Comments
    fields = ['text']
    success_url = '/'


    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.owner = self.request.user
            return super().form_valid(form)
        else:
            messages.add_message(self.request, messages.ERROR, 'Необходимо авторизоваться что бы оставлять комменты')
            return redirect("/")



    # def post(self, request, *args, **kwargs):
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         Comments.objects.update_or_create(
    #             owner=self.request.user,
    #             text=request.POST.get('text')
    #         )
    #         return redirect('/')
    #     else:
    #         return HttpResponse(status=400)
    #
    #
class AddLinkView(CreateView):
    model = Links
    fields = ['description', 'link']
    success_url = 'links'


