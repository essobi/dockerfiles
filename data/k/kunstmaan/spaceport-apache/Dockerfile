FROM ubuntu:16.04  
MAINTAINER Ruud Denviel <ruud.denivel@kunstmaan.be>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C  
  
RUN echo 'deb http://ppa.launchpad.net/ondrej/php/ubuntu xenial main' >>
/etc/apt/sources.list && \  
apt-get -y -q update && \  
apt-get -y -q install apache2 vim && \  
apt-get -y -q autoremove && \  
apt-get -y -q clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN a2enmod \  
autoindex \  
deflate \  
expires \  
filter \  
headers \  
include \  
mime \  
rewrite \  
setenvif \  
ssl \  
proxy_html \  
proxy_http \  
proxy_fcgi \  
xml2enc \  
mpm_event  
  
RUN a2dismod \  
mpm_prefork \  
mpm_worker  
  
RUN mkdir -p /etc/ssl/certs && \  
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout
/etc/ssl/certs/selfsigned.key -out /etc/ssl/certs/selfsigned.crt -subj
"/C=BE/ST=Vlaams-Brabant/L=Leuven/O=Kunstmaan/OU=Development/CN=$*.docker"  
  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
  
COPY tuning.conf /etc/apache2/conf-available/tuning.conf  
RUN ln -sf /etc/apache2/conf-available/tuning.conf /etc/apache2/conf-
enabled/tuning.conf  
  
ADD run.sh /scripts/run.sh  
ADD default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN chmod -R 755 /scripts  
  
CMD ["/scripts/run.sh"]  
  
WORKDIR /app  
  
EXPOSE 80  
EXPOSE 443  

