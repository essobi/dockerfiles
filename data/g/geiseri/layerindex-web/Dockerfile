FROM debian:jessie  
  
MAINTAINER Ian Reinhart Geiser "geiseri@yahoo.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
## get base system  
RUN apt-get -qq update && \  
apt-get install -y git-core python-git python-dev python-pip nano \  
build-essential nginx supervisor sqlite3 uwsgi-plugin-python  
  
## install layerindex  
RUN mkdir -p /home/docker/code && mkdir -p /home/docker/layers && \  
git clone git://git.yoctoproject.org/layerindex-web /home/docker/code/app && \  
pip2 install -r /home/docker/code/app/requirements.txt  
  
## Configure nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf && \  
rm /etc/nginx/sites-enabled/default  
  
ADD nginx-app.conf /etc/nginx/sites-enabled/nginx-app.conf  
ADD supervisor-app.conf /etc/supervisor/conf.d/supervisor-app.conf  
ADD uwsgi.ini /home/docker/code/uwsgi.ini  
ADD uwsgi_params /home/docker/code/uwsgi_params  
ADD wsgi.py /home/docker/code/app/wsgi.py  
  
## Configure webapp  
ADD settings.py /home/docker/code/app/settings.py  
RUN cd /home/docker/code/app/ && \  
python2 manage.py syncdb --noinput && \  
python2 manage.py migrate && \  
echo "from django.contrib.auth.models import User;
User.objects.create_superuser('admin', 'admin@localhost', 'admin')" | python2
manage.py shell  
  
EXPOSE 80  
CMD ["supervisord", "-n"]  

