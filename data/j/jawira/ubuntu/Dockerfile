FROM ubuntu:18.04  
  
MAINTAINER Jawira Portugal  
  
  
#Installing Docker  
#-----------------  
RUN apt-get update && \  
apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
  
RUN add-apt-repository -y "deb [arch=amd64]
https://download.docker.com/linux/ubuntu artful stable"  
#RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  
  
RUN apt-get update && \  
apt-get install -y docker-ce && \  
docker -v  
  
  
#Installing required software  
#----------------------------  
RUN apt-get install -y \  
make \  
wget  
  
  
#Installing PHP  
#--------------  
#https://serverfault.com/questions/683605/docker-container-time-timezone-will-
not-reflect-changes  
ENV TZ=Europe/Brussels  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get install -y \  
php7.2 \  
php7.2-cli  
# php7.2-common \  
# php7.2-curl \  
# php7.2-dev \  
# php7.2-json \  
# php7.2-ldap \  
# php7.2-mysql \  
# php7.2-opcache \  
# php7.2-readline \  
# php7.2-tidy \  
# php7.2-xml \  
# php7.2-xmlrpc \  
# php7.2-bz2 \  
# php7.2-fpm \  
# php7.2-imap \  
# php7.2-intl \  
# php7.2-mbstring \  
# php7.2-soap \  
# php7.2-xsl \  
# php7.2-zip  
#Cleaning  
#--------  
RUN apt-get autoremove -y && apt-get autoclean && apt-get clean && rm -rf
/tmp/* /var/tmp/* /var/lib/apt/lists/*  

