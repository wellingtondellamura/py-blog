from django.shortcuts import render

# Create your views here.

def principal(request):

    context = {}
    context['title'] = 'Blog'

    lista_posts = Post.objects.filter(publicado=True)

    form = BuscaPostForm(request.POST or None)
    if form.is_valid():
        busca = form.cleaned_data.get('busca')
        cidades = form.cleaned_data.get('cidades')
        if busca:
            lista_posts = lista_posts.filter(Q(titulo__contains=busca) | Q(texto__contains=busca))
        if cidades:
            lista_posts = lista_posts.filter(cidade__in=cidades)

    context['form'] = form
    context['lista_posts'] = lista_posts

    return render(request, 'blog/principal.html', context)

def sugerir_post(request):

    context = {}
    context['title'] = 'Blog'
    context['subtitle'] = 'Sugerir post'

    form = SugestaoPostForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Cadastrado com sucesso.')
        return redirect('/')

    context['form'] = form

    return render(request, 'blog/sugerir_post.html', context)