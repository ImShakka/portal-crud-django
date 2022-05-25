from django.db import models

class Writer(models.Model):
    # nome do autor/escritor
    name = models.CharField(max_length=255)
    # data de nascimento do autor/escritor
    birth_date = models.DateField()
    # email do autor/escritor
    email = models.EmailField()

class Publisher(models.Model):
    # nome da editora
    name = models.CharField(max_length=255)
    # cidade da editora
    city = models.CharField(max_length=255)
    # estado da editora
    state = models.CharField(max_length=2)

class Format(models.Model):
    # nome do formato
    name = models.CharField(max_length=255)

class Book(models.Model):
    # titulo do livro
    title = models.CharField(max_length=255)
    # subtitulo do livro
    subtitle = models.CharField(max_length=255)
    # autor/escritor do livro
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    # editora de publicacao do livro
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    # formato do livro
    format = models.ForeignKey(Format, on_delete=models.CASCADE)
    # data de lancamento do livro
    release_date = models.DateField()
    # ISBN do livro
    isbn = models.CharField(max_length=255)
    # numero de paginas do livro
    pages_number = models.PositiveBigIntegerField()