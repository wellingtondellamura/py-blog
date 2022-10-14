from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField('Nome', max_length=100)
    initials = models.CharField('Sigla', max_length=2, default='  ')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['name']

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField('Nome', max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, verbose_name='Estado')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = 'Cidade'
        verbose_name_plural = 'Cidades'
        ordering = ['name']

    def __str__(self):
        return self.name + ' - ' + self.state.name

class Post(models.Model):
    title = models.CharField('Título', max_length=100)
    subtitle = models.CharField('Subtítulo', max_length=100)
    content = models.TextField('Conteúdo')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name='Cidade')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Categoria')
    published = models.BooleanField('Publicado?', default=True)
    image = models.ImageField('Imagem', upload_to='blog/uploads', null=True, blank=True)
    keywords = models.CharField('Palavras-chave', max_length=255, help_text='Palavras-chave separadas por vírgula')

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail')
    comment = models.TextField('Comentário')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Postagem')

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['name']

    def __str__(self):
        return self.name


class PostSuggestion(models.Model):

    titulo = models.CharField(verbose_name='Título', max_length=50, null=False, blank=False)
    email = models.EmailField('E-mail')

    class Meta:
        verbose_name = 'Sugestão de Post'
        verbose_name_plural = 'Sugestões de Posts'

    def __str__(self):
        return self.titulo


