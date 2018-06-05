FROM php:7.0-apache  
  
LABEL Author="desertraider"  
  
RUN apt update && apt install -y wget unzip vim rsync  
COPY /php.ini /usr/local/etc/php/  
COPY /WikiData.zip /  
COPY /LocalSettings.php /  
RUN docker-php-ext-install -j$(nproc) mysqli  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libtidy-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
RUN docker-php-ext-install -j$(nproc) tidy  
#RUN apt-get install -y php-curl php-gd php-tidy php-mysql  
#RUN cd /var/www/html/ && ls && cd /var/www/ && rm -vrf html  
#RUN wget https://downloads.sourceforge.net/project/bluespice/BlueSpice-
free-2.27.2-installer.zip --content-disposition  
RUN mv /WikiData.zip /wiki.zip  
RUN mkdir /var/www/html/wiki  
RUN unzip /wiki.zip -d /var/www/html/wiki && rm -vf /wiki.zip  
RUN rm -vf /var/www/html/wiki/LocalSettings.php  
COPY /LocalSettings.php /var/www/html/wiki/  
RUN chmod -Rv 777 /var/www/html/wiki/cache  
RUN chmod -Rv 777 /var/www/html/wiki/extensions/BlueSpiceFoundation/config  
RUN chmod -Rv 777 /var/www/html/wiki/extensions/BlueSpiceFoundation/data  
#EXPOSE 80  
#CMD [ "/usr/sbin/apache2ctl", "-D", "FOREGROUND" ]

