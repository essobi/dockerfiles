  
FROM debian:jessie-slim  
  
LABEL maintainer "ryan.e.t@gmail.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NGINX_SERVERNAME hamwan.net  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
git \  
python \  
python-dev \  
python-setuptools \  
python-pip \  
nginx \  
supervisor \  
sudo \  
libpq-dev && \  
pip install -U pip setuptools && \  
pip install uwsgi \  
django==1.6.6 \  
south \  
psycopg2 \  
django-debug-toolbar \  
ipaddr \  
pyasn1 && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
COPY . /home/docker/code/hamwan-portal/  
RUN ln -sf /home/docker/code/hamwan-
portal/virtualization/Docker/portal/portal_nginx.conf /etc/nginx/sites-
available/default && \  
ln -sf /home/docker/code/hamwan-
portal/virtualization/Docker/portal/supervisor.conf /etc/supervisor/conf.d/  
  
RUN git clone https://github.com/HamWAN/django-ssl-client-auth.git
/home/docker/code/django-ssl-client-auth  
RUN mkdir /home/docker/code/hamwan-portal/static && \  
mkdir /home/docker/code/hamwan-portal/media  
  
VOLUME ["/home/docker/code/hamwan-portal/hamwanadmin/", "/etc/nginx/ssl/",
"/etc/nginx/sites-available/"]  
  
EXPOSE 80  
CMD ["supervisord", "-n"]  

