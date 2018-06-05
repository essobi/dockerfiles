FROM debian:jessie  
  
RUN apt-get update --fix-missing && \  
apt-get install -y apt-transport-https lsb-release ca-certificates vim wget
git zip unzip && \  
wget -O /etc/apt/trusted.gpg.d/php.gpg https://packages.sury.org/php/apt.gpg
&& \  
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list && \  
apt-get update --fix-missing && \  
apt-get install -y php7.1 php7.1-mysql php7.1-xml php7.1-mbstring \  
php7.1-xmlrpc php7.1-curl apache2  
  
EXPOSE 80  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
COPY config/php.ini /etc/php/7.1/apache2/php.ini  
  
COPY config/virtualhost-apache.conf /etc/apache2/sites-
available/000-default.conf  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
  

