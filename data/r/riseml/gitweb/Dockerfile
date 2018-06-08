# build  
# docker build . -t gitweb  
# run (prd)  
# docker run -ti -v /git:/git -p 8888:8888 gitweb  
# run (dev)  
# docker run -ti -v $(pwd)/git:/git -p 8888:8888 gitweb  
FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update --fix-missing && \  
apt-get -y install git apache2 libapache2-mod-wsgi \  
build-essential python-dev curl supervisor  
  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python get-pip.py && \  
rm get-pip.py  
  
COPY requirements.lock /app/requirements.lock  
RUN pip install -r /app/requirements.lock  
  
ENV APACHE_RUN_DIR /var/run  
ENV APACHE_LOCK_DIR /var/lock  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME localhost  
ENV PORT 8888  
EXPOSE 8888  
ENV GIT_ROOT /git  
ENV SYNC_ROOT /sync  
  
RUN usermod -u 1000 www-data && \  
chown -R www-data:www-data /var/www && \  
groupmod -g 1000 www-data && \  
a2enmod env alias cgid && \  
a2dismod mpm_*  
  
RUN mkdir -p /app && \  
chown www-data:www-data /app  
  
RUN mkdir -p /sync && \  
chown www-data:www-data /sync  
  
RUN mkdir -p /var/log/supervisord && chown www-data:www-data
/var/log/supervisord  
  
RUN chsh -s /bin/bash www-data && su -c "git config --global push.default
simple" www-data  
  
COPY apache2.conf /etc/apache2/apache2.conf  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY rsyncd.conf /etc/rsyncd.conf  
COPY . /app  
CMD if [ -z $CLUSTER_ID ]; then echo "cluster id not set"; exit 1; else chown
www-data:www-data /git && /usr/bin/supervisord -n -c
/etc/supervisor/conf.d/supervisord.conf; fi  

