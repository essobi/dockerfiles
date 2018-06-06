FROM debian:9  
MAINTAINER Jakub Kwiatkowski <jakub@ajbisoft.pl>  
RUN apt-get update && apt-get install -y apt-transport-https  
COPY sources.list /etc/apt/  
COPY apt.gpg /etc/apt/trusted.gpg.d/php.gpg  
RUN apt-get update && apt-get install -y apache2 php7.1 php7.1-mbstring
php7.1-xml php7.1-zip \  
&& apt-get -y --purge autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/*  
COPY 000-default.conf /etc/apache2/sites-available/  
COPY apache2.conf /etc/apache2/  
RUN a2enmod rewrite  
COPY docker-entrypoint.sh /  
WORKDIR /var/www  
EXPOSE 80  
ENTRYPOINT ["/bin/sh", "/docker-entrypoint.sh"]  

