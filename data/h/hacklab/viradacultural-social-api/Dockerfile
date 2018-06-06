FROM ubuntu:trusty  
MAINTAINER Fabio Montefuscolo <fabio.montefuscolo@hacklab.com.br>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN useradd -m -u 1000 -s /bin/bash runner  
RUN mkdir -p /srv/app \  
&& mkdir -p /srv/webfiles/static \  
&& mkdir -p /srv/webfiles/media \  
&& mkdir -p /srv/webfiles/media/map_pictures  
  
COPY . /srv/app  
WORKDIR /srv/app  
  
RUN ./install_os_dependencies.sh upgrade  
RUN apt-get install -y nginx supervisor  
  
RUN pip install -r requirements/production.txt \  
&& pip install -r requirements/local.txt  
  
RUN chown -R runner *  
  
ENV PYTHONPATH='/srv/app'  
ENV GUNICORN_LOG_LEVEL='info'  
ENV GUNICORN_EXTRA_FLAGS=''  
ENV DATABASE_URL='postgis://viradauser:viradapass@postgis/virada'  
  
ENV DJANGO_SECRET_KEY='pass-a-valid-one-at-docker-run'  
ENV DJANGO_CORS=true  
ENV DJANGO_SETTINGS_MODULE='config.settings.production'  
ENV DJANGO_MEDIA_ROOT='/srv/webfiles/media/'  
ENV DJANGO_STATIC_ROOT='/srv/webfiles/static/'  
  
ENV MAP_PICTURES_PATH='/srv/webfiles/media/map_pictures'  
ENV
MAP_PICTURES_MASK_FILE_PATH='/srv/app/viradacultural_social_api/static/mask.png'  
ENV MAP_PICTURES_BASE_URL='/media/map_pictures'  
ENV MAP_PICTURES_SIZE=36  
  
RUN python manage.py collectstatic --noinput  
  
USER root  
EXPOSE 80 8000  
CMD ["supervisord", "-c", "/srv/app/docker/supervisord.conf"]  

