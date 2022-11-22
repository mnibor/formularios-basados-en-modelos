from django.db import models

# Create your models here.
options = [
    [0, 'Pedido de información'],
    [1, 'Queja por un producto'],
    [2, 'Felicitaciones'],
    [3, 'Otras']
]

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre y Apellido')
    email = models.EmailField(verbose_name='Correo electrónico')
    message = models.TextField(verbose_name='Mensaje')
    contact_type = models.IntegerField(choices=options, verbose_name='Tipo de contacto')
    subscription = models.BooleanField(default=False, verbose_name='Suscribirme a correos informativos')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')

    class Meta:
        verbose_name = 'Mensaje'
        verbose_name_plural = 'Mensajes'
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name