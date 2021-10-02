from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Evento(models.Model):
    titulo = models.CharField(max_length = 100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do evento')
    # verbose_name cria um apelido para o campo data_evento.
    data_criacao = models.DateTimeField(auto_now=True)#Sempre que for inserido
    #um regitro ele automaticamente insere a hora atual.
    usuario = models.ForeignKey(User, on_delete= models.CASCADE)


    class Meta:
        db_table = 'evento'#Define o nome da tabela. se nao for definico,
        # o comando migrate coloca

    def __str__(self):  # Qdo o django acesso o abjeto aparece 'evento object(1)
        return self.titulo   # porque nao falamos como o objeto sera tratado
                            # com o metodo __str__ sempre q for chamado o objeto
                            # titulo, o django trará o nome do titulo.
