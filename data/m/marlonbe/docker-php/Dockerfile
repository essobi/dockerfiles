FROM sameersbn/mysql:latest  
MAINTAINER PHP marlon <php@marlon.be>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y --fix-missing && \  
apt-get install -y locales  
  
RUN locale-gen nl_BE.UTF-8  
ENV LC_ALL nl_BE.UTF-8  
  
RUN apt-get -y -f install software-properties-common && \  
add-apt-repository ppa:ondrej/php && \  
apt-get update -y  
  
# PHP + extensions  
RUN apt-get -y -f --force-yes install php7.2-cli php7.2-dev php7.2-mysql
php7.2-xmlrpc php7.2-curl curl libicu-dev php7.2-sqlite php-memcached php-pear
php7.2-xsl php7.2-gd php7.2-intl php7.2-mbstring php7.2-bcmath php7.2-zip
php7.2-soap  

