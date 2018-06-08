FROM ruby:2.5.1  
ENV DEBIAN_FRONTEND noninteractive  
ENV NGINX_VERSION 1.13.12-1~stretch  
ENV NOKOGIRI_USE_SYSTEM_LIBRARIES 1  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libxml2 libxml2-dev libxslt1-dev
nodejs rsyslog unzip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-key adv --fetch-keys http://nginx.org/keys/nginx_signing.key \  
&& echo "deb http://nginx.org/packages/mainline/debian/ stretch nginx" >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --no-install-suggests -y \  
ca-certificates \  
nginx=${NGINX_VERSION} \  
gettext-base \  
&& rm -rf /var/lib/apt/lists/*  
COPY files/nginx.conf /etc/nginx/nginx.conf  
  
COPY files/rsyslog.conf /etc/rsyslog.conf  
COPY files/21-nginx-loggly.conf /etc/rsyslog.d/21-nginx-loggly.conf  
COPY files/rsyslog.sh /rsyslog.sh  
  
ENV ENVCONSUL_VERSION 0.7.3  
RUN cd /tmp \  
&& wget
https://releases.hashicorp.com/envconsul/${ENVCONSUL_VERSION}/envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip
\  
&& unzip envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip \  
&& mv envconsul /usr/local/bin/envconsul \  
&& rm envconsul_${ENVCONSUL_VERSION}_linux_amd64.zip  
  
RUN chmod 755 /rsyslog.sh  

