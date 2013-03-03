from django.http import HttpResponse
import urllib2


# Podem ser usados outros webservices como o http://ceplivre.pc2consultoria.com/index.php?module=cep&cep=%s&formato=xml
# Entretanto deve ser observado o encoding para que ele seja alterado na linha 10
# Outra referencia util http://allissonazevedo.com/2012/03/22/buscando-cep-diretamente-pelo-site-dos-correios-em-python/
def addressGet(request, zipcode):
    url = "http://viavirtual.com.br/webservicecep.php?cep=" + zipcode
    page = urllib2.urlopen(url)
    text = page.read().decode('iso-8859-1').encode('utf8')
    splitted = text.split('||')
    return HttpResponse('{"street":"%s","district":"%s","city":"%s","state":"%s"}' % (splitted[0], splitted[1], splitted[2], splitted[4]))
