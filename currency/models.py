from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _


class ExchargeRate(models.Model):
    currency_code = models.CharField(_('Código moeda entrada', ), max_length=6)
    currency_code_in = models.CharField(_('Codigo moeda saida', ), max_length=6)
    bid = models.DecimalField(_('Compra'), max_digits=16, decimal_places=5, default=0.00)
    ask = models.DecimalField(_('Venda'), max_digits=16, decimal_places=5, default=0.00)
    date_in = models.CharField(_('Data da cotação(em segundos)'), max_length=100)
    creation_datetime = models.DateTimeField(_("Data de criação"), editable=False)
    edition_datetime = models.DateTimeField(_("Última atualização"), null=True, blank=True)

    def __str__(self):
        value = str(self.id)
        if self.currency_code and self.currency_code_in:
            value = "Cotação: {} - {}".format(self.currency_code, self.currency_code_in)
            
        return value
    
    class Meta:
        ordering = ('-creation_datetime',)
        db_table = _('excharge_rates')
        verbose_name = _('Taxa de câmbio')
        verbose_name_plural = _('Taxas de câmbio')
    
    def save(self, *args, **kwargs):
        # Atualiza datas de criação e edição
        if not self.creation_datetime:
            self.creation_datetime = timezone.now()
        self.edition_datetime = timezone.now()
        return super(ExchargeRate, self).save(*args, **kwargs)