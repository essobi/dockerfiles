FROM ubuntu:16.04  
MAINTAINER Emad Shaaban <emad@bizzotech.com>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
ENV WKHTMLTOX_VERSION 0.12.4  
ENV DOCKERIZE_VERSION v0.5.0  
  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties curl && \  
apt-key adv --recv-keys \--keyserver hkp://keyserver.ubuntu.com:80
0xcbcb082a1bb943db && \  
add-apt-repository "deb
http://ams2.mirrors.digitalocean.com/mariadb/repo/10.0/ubuntu xenial main" &&
\  
curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get update && \  
apt-get install -y --allow-unauthenticated sudo wget nodejs python-mysqldb \  
git build-essential python-setuptools python-dev libffi-dev libssl-dev \  
ntp screen mariadb-common libmariadbclient-dev mariadb-client \  
libxslt1.1 libxslt1-dev libcrypto++-dev postfix libtiff5-dev libjpeg8-dev \  
liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk zlib1g-dev
libfreetype6-dev \  
python-pip fontconfig libxrender1 libxext6 xfonts-75dpi xfonts-base && \  
rm -rf /var/lib/apt/lists/* && \  
wget
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/${WKHTMLTOX_VERSION}/wkhtmltox-${WKHTMLTOX_VERSION}_linux-
generic-amd64.tar.xz && \  
tar xf wkhtmltox-${WKHTMLTOX_VERSION}_linux-generic-amd64.tar.xz && \  
mv wkhtmltox/bin/* /usr/local/bin/ && \  
rm wkhtmltox-${WKHTMLTOX_VERSION}_linux-generic-amd64.tar.xz && \  
wget
https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-
linux-amd64-${DOCKERIZE_VERSION}.tar.gz && \  
tar -C /usr/local/bin -xzvf dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz
&& \  
rm dockerize-linux-amd64-${DOCKERIZE_VERSION}.tar.gz && \  
pip install --upgrade setuptools pip  

