# Imagr Dockerfile  
# Version 0.3  
FROM ubuntu:14.04.1  
MAINTAINER Graham Gilbert <graham@grahamgilbert.com>  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
ENV APPNAME Imagr  
ENV APP_DIR /home/docker/imagr  
ENV TZ Europe/London  
ENV DOCKER_IMAGR_TZ Europe/London  
ENV DOCKER_IMAGR_ADMINS Docker User, docker@localhost  
ENV DOCKER_IMAGR_LANG en_GB  
ENV DOCKER_IMAGR_DISPLAY_NAME Imagr Server  
  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get -y update && \  
add-apt-repository -y ppa:nginx/stable && \  
apt-get -y install \  
git \  
python-setuptools \  
nginx \  
postgresql \  
postgresql-contrib \  
libpq-dev \  
python-dev \  
supervisor \  
nano \  
libffi-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN easy_install pip && \  
git clone https://github.com/grahamgilbert/imagr_server.git $APP_DIR && \  
pip install -r $APP_DIR/requirements.txt && \  
pip install psycopg2==2.5.3 && \  
pip install gunicorn && \  
pip install setproctitle  
  
ADD nginx/nginx-env.conf /etc/nginx/main.d/  
ADD nginx/imagr.conf /etc/nginx/sites-enabled/imagr.conf  
ADD nginx/nginx.conf /etc/nginx/nginx.conf  
ADD settings.py $APP_DIR/imagr_server/  
ADD settings_import.py $APP_DIR/imagr_server/  
ADD wsgi.py $APP_DIR/  
ADD gunicorn_config.py $APP_DIR/  
ADD django/management/ $APP_DIR/imagr_server/management/  
ADD run.sh /run.sh  
ADD supervisord.conf $APP_DIR/supervisord.conf  
  
RUN update-rc.d -f postgresql remove && \  
update-rc.d -f nginx remove && \  
rm -f /etc/nginx/sites-enabled/default && \  
mkdir -p /home/app && \  
mkdir -p /home/backup && \  
ln -s $APP_DIR /home/app/imagr  
  
EXPOSE 8000  
CMD ["/run.sh"]  

