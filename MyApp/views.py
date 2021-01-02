from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from MyApp.forms import CommentForm, EditUserForm, ProfileForm
from MyApp.models import Comments, Links, LinksThemes, Profile


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


class UpdateProfileView(UpdateView):
    model = User
    form_class = EditUserForm
    second_form_class = ProfileForm
    template_name = 'MyApp/profile.html'
    success_url = '/'

    # def get_context_data(self, **kwargs):
    #     context = super(UpdateProfileView, self).get_context_data(**kwargs)
    #     #context['active_client'] = True
    #     if 'form' not in context:
    #         context['form'] = self.form_class(self.request.GET, instance=self.request.user)
    #     if 'form2' not in context:
    #         context['form2'] = self.second_form_class(self.request.GETj, instance=self.request.user.profile)
    #     context['active_client'] = True
    #     return context

    def get(self, request, **kwargs):
        self.object = User.objects.get(pk=self.request.user.pk)
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(master=self.request.user)
        form = self.form_class(self.request.GET, instance=self.request.user)
        form2 = self.second_form_class(self.request.GET, instance=self.request.user)
        context = self.get_context_data(object=self.object, form=form, form2=form2)
        return self.render_to_response(context)

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=request.user)
        if not hasattr(request.user, 'profile'):
            Profile.objects.create(master=self.request.user)
        form2 = self.second_form_class(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and form2.is_valid():
            form.save()
            m = Profile.objects.get(master=self.request.user)
            m.photo = form2.cleaned_data['photo']
            m.country = form2.cleaned_data['country']
            m.save()
            messages.success(self.request, 'Settings saved successfully')
            return HttpResponseRedirect(self.get_success_url())
        else:
            print('form invalid')
            print(form.errors)
            return self.render_to_response(
                self.get_context_data(form=form, form2=form2))


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


