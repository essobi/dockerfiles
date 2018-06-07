FROM debian:jessie  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-heroku"  
LABEL version="latest"  
  
RUN apt-get update --fix-missing && \  
apt-get update && \  
apt-get install -y -q git wget apache2 php5 php5-mysql php5-json php5-fpm
libapache2-mod-php5 sudo && \  
ln -s /usr/sbin/php5-fpm /usr/sbin/php-fpm && \  
ln -s /usr/sbin/apache2 /usr/sbin/httpd  
  
RUN wget https://getcomposer.org/installer -O - -q | php -- --install-
dir=/usr/local/bin --filename=composer && \  
wget https://cli-assets.heroku.com/branches/stable/heroku-linux-amd64.tar.gz
-O heroku.tar.gz && \  
tar -xvzf heroku.tar.gz -C /usr/local/lib && \  
/usr/local/lib/heroku/install  
  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
chown ${uid}:${gid} -R /home/developer  
  
WORKDIR /home/developer/workspace/  
  
RUN a2enmod proxy_fcgi  
USER developer  
RUN /usr/local/bin/heroku update  
USER root  
  
COPY heroku-wrap /heroku-wrap  
RUN chmod +x /heroku-wrap  
  
ENV APACHE_RUN_USER=www-data \  
APACHE_RUN_GROUP=www-data \  
APACHE_LOG_DIR=/var/log/apache2 \  
APACHE_LOCK_DIR=/var/lock/apache2 \  
APACHE_RUN_DIR=/var/run/apache2 \  
APACHE_PID_FILE=/var/run/apache2/apache2.pid  
  
ENTRYPOINT [ "/heroku-wrap" ]  

