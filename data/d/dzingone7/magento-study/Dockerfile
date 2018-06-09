FROM ubuntu:latest  
MAINTAINER Arvind Rawat (arvindr226@gmail.com)  
  
  
RUN mkdir /var/www/  
RUN mkdir /var/www/html  
ADD codice/ /var/www/html  
  
#RUN apt-get update && apt-get install -y git  
#RUN git clone --branch 2.1.7 https://github.com/magento/magento2.git
/var/www/html  
# install dependencies  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apache2 \  
ca-certificates openssl \  
curl \  
php7.0 \  
php7.0-curl \  
php7.0-gd \  
php7.0-json \  
php7.0-simplexml \  
php7.0-mbstring \  
php7.0-mysql \  
php7.0-zip \  
php-soap \  
openssh-server \  
composer \  
php7.0-mcrypt \  
php7.0-intl \  
supervisor \  
libapache2-mod-php7.0 \  
&& rm -r /var/lib/apt/lists/*  
RUN sed -i '/<Directory \/var\/www\/>/,/<\/Directory>/ s/AllowOverride
None/AllowOverride All/' /etc/apache2/apache2.conf  
RUN a2enmod rewrite expires  
RUN a2enmod ssl  
RUN a2enmod headers  
  
# COPY code/ /var/www/html  
RUN mkdir /var/run/sshd  
RUN echo 'root:screencast' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/g'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN apt-get update  
RUN cd /var/www/html && ls && composer install  
RUN service apache2 restart  
RUN chmod -R 777 /var/www/html/app/ var/www/html/var/ var/www/html/pub  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN cd var/www/  
  
## Mount ##  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
# Default command  
#CMD ["apachectl", "-D", "FOREGROUND"]  
# Ports  
#RUN service apache2 restart  
#RUN apt-get update  
#RUN cd /var/www/html && ls && composer install  
EXPOSE 80  
EXPOSE 443  
EXPOSE 22  
CMD ["/usr/bin/supervisord"]  
  

