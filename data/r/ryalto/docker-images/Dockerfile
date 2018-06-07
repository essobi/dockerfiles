FROM ruby:2.4.1  
MAINTAINER paul@trippett.org  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NGINX_VERSION 1.13.0-1~jessie  
ENV NOKOGIRI_USE_SYSTEM_LIBRARIES 1  
##  
## Install NodeJS to prevent any ExecJS issues  
##  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libxml2 libxml2-dev libxslt1-dev
nodejs rsyslog unzip && \  
rm -rf /var/lib/apt/lists/*  
  
##  
## Install NGINX  
##  
RUN apt-key adv --fetch-keys http://nginx.org/keys/nginx_signing.key \  
&& echo "deb http://nginx.org/packages/mainline/debian/ jessie nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
ADD files/nginx.conf /etc/nginx/nginx.conf  
  
##  
## Configure rsyslogd  
##  
ADD files/rsyslog.conf /etc/rsyslog.conf  
ADD files/21-nginx-loggly.conf /etc/rsyslog.d/21-nginx-loggly.conf  
ADD files/rsyslog.sh /rsyslog.sh  
  
##  
## Configure envconsul  
##  
ENV ENVCONSUL_VERSION 0.6.2  
RUN cd /tmp \  
&& wget
https://releases.hashicorp.com/envconsul/${ENVCONSUL_VERSION}/envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip
\  
&& unzip envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip \  
&& mv envconsul /usr/local/bin/envconsul \  
&& rm envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip  
  
##  
## Setup Start command  
##  
RUN chmod 755 /rsyslog.sh  

