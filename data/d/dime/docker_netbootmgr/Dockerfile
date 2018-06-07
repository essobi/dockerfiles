FROM django:latest  
MAINTAINER Dominic S. "docker@dominic86.de"  
RUN pip install
https://git.dominic86.de/netbootmgr/django_netbootmgr/archive/stable.tar.gz &&
\  
pip install django-jenkins coverage pep8 pyflakes  
  
RUN mkdir -p /app/data && \  
mkdir -p /app/src && \  
mkdir -p /app/django_netbootmgr && \  
mkdir -p /app/reports  
  
COPY conf /app/src/django_netbootmgr_template  
  
COPY init.sh /app/init  
  
RUN useradd -M -u 1000 -d /app django && \  
django-admin startproject --template=/app/src/django_netbootmgr_template
django_netbootmgr /app && \  
chown django:django /app -R && \  
chmod 500 /app/init  
  
WORKDIR /app  
  
VOLUME ["/app/reports"]  
  
CMD ["/app/init"]

