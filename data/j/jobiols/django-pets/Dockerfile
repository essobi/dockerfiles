FROM ubuntu:14.04  
MAINTAINER jobiols <jorge.obiols@gmail.com>  
  
# Fuentes de inspiración  
# http://www.secnot.com/docker-nginx-gunicorn-django.html  
# https://glyph.twistedmatrix.com/2015/03/docker-deploy-double-dutch.html  
  
# Actualizacion de los 'sources' a la ultima version  
RUN apt-get update  
  
# Instalar los paquetes del sistema necesarios para python  
RUN apt-get install -qy python \  
python-dev \  
python-pip \  
python-setuptools \  
build-essential  
  
# Instalar algunas utilidades extras (opcional)  
RUN apt-get install -qy vim \  
wget \  
net-tools \  
git  
  
# Instalamos resto aplicaciones  
RUN apt-get install -qy nginx \  
supervisor  
  
# Activar un virtualenv para tener python 3.4.3  
RUN apt-get install -qyy \  
-o APT::Install-Recommends=false -o APT::Install-Suggests=false \  
python-virtualenv  
RUN virtualenv --python=`which python3` /appenv  
  
# instalar pip en python 3 (aca no funciona source)  
RUN . /appenv/bin/activate; pip install pip==9.0.1  
  
###############################  
#  
# Nginx  
#  
###############################  
  
# Copiamos la configuracion de nginx  
ADD nginx-default /etc/nginx/sites-available/default  
  
# Se desactiva el modo demonio para arrancar el proceso con supervisor  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
# Cambiar usuario de root a www-data (por defecto en ubuntu 14.04)  
# RUN echo "user www-data;" >> /etc/nginx/nginx.conf  
  
# agregar logging  
# RUN echo "user www-data;" >> /etc/nginx/nginx.conf  
  
# Permisos  
RUN chown -R www-data:www-data /var/lib/nginx  
  
# Permitimos el acceso al puerto 80 del contenedor  
EXPOSE 80  
  
  
##################################  
#  
# Gunicorn y Django  
#  
################################  
  
# Copiar aplicacion del subdirectorio django_app/ a la imagen y ajustar
permisos  
ADD django_app /django_app  
RUN chown -R www-data:www-data /django_app  
  
# Si la aplicacion tiene dependencias de paquetes del del sistema  
# este es un buen sitio para instalarlas, por ejemplo:  
# RUN apt-get install -qy python-dev libjpeg-dev zlib1g-dev  
  
# Usamos requirements.txt para instalar las dependencias sobre python 3  
RUN . /appenv/bin/activate; pip install -r /django_app/requirements.txt  
  
# Una buena medida de seguridad es alamacenar claves usuarios y  
# otras credenciales de seguridad en variables de entorno.  
# Se importan desde settings.py con:  
# PAYPAL_CLIENT_ID = os.environ['PAYPAL_CLIENT_ID']  
# PAYPAL_CLIENT_SECRET = os.environ['PAYPAL_CLIENT_SECRET']  
#ENV PAYPAL_CLIENT_ID sdfasFASDRwefasFqasdfAsdfAsdFAsdfsDFaSDfWERtSDFg  
#ENV PAYPAL_CLIENT_SECRET ASAsdfarasDFaRasdFaSsdfghJdfGHDGsdTRSDfGErtAFSD  
  
# Por ultimo se copia la configuracion de gunicorn.  
ADD gunicorn-config.py /etc/gunicorn/config.py  
  
  
#############################  
#  
# Supervisor  
#  
############################  
  
# Copiar la configuracion  
ADD supervisor.conf /etc/supervisor/conf.d/django_app.conf  
  
# Instalamos supervisor-stdout para que los logs de supervisor, sean impresos  
# en stdout, asi podran ser grabados fuera del contenedor sin necesidad  
# de montar volumenes. (ver supervisor.conf)  
  
# este se instala con python 2  
RUN pip install supervisor-stdout  
  
# Establecer el directorio de trabajo  
WORKDIR /django_app  
  
# Comando por defecto que se ejecutara al arranque del contenedor, supervisor  
# se encarga de gestionar nginx y gunicorn.  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]  
  

