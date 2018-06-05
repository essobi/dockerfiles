FROM php:5.6.16-apache  
# Install modules  
RUN apt-get update && apt-get install -y \  
git \  
php5-mysql \  
libmcrypt-dev \  
&& docker-php-ext-configure mbstring --enable-mbstring \  
&& docker-php-ext-install pdo_mysql mcrypt mbstring bcmath  
RUN a2enmod rewrite  
#RUN a2enmod ssl  
COPY sites-available/ /etc/apache2/sites-available/  
COPY config/php.ini /usr/local/etc/php/  
  
RUN a2ensite manage.unblockr.net  
#RUN a2ensite manage.unblockr.net-ssl  
RUN pear channel-discover pear.nrk.io && pear install nrk/Predis  
RUN git clone https://github.com/bobthecow/mustache.php.git /mustache  
  
RUN mkdir /vpn  
ADD https://github.com/OpenVPN/easy-
rsa/releases/download/v3.0.3/EasyRSA-3.0.3.tgz /tmp/  
WORKDIR /vpn  
RUN tar xvzf /tmp/EasyRSA-3.0.3.tgz  
RUN mv EasyRSA-3.0.3 easyrsa  
RUN mkdir /vpn/pki  
ENV PATH=${PATH}:/vpn/easyrsa  
VOLUME /vpn/pki  
  
EXPOSE 80  

