FROM ubuntu:trusty  
MAINTAINER Milo van der Linden <milo@dogodigi.net>  
  
# Install base packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
git \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-curl \  
php-pear \  
php-apc && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN /usr/sbin/php5enmod mcrypt  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
#Defaults, modify with environment variable to change  
ENV ALLOW_OVERRIDE **False**  
ENV MYSQL_DATABASE buurtpreventie  
ENV DB_PORT_3306_TCP_ADDR localhost  
ENV DB_PORT_3306_TCP_PORT 3306  
ENV DB_ENV_MYSQL_USER root  
ENV DB_ENV_MYSQL_PASS mypassword  
ENV APP_LOCALE nl  
ENV APP_SECRET SecretTokenForApplication  
ENV APP_AUTHOR Buurtpreventie  
ENV APP_TITLE Buurtpreventie  
ENV APP_DESCRIPTION 'Buurtpreventie in Eindhoven'  
ENV APP_MIN_WALKERS 2  
ENV APP_MONTHS 3  
ENV APP_SHOW_RESULT true  
  
# Add image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Configure /webdir folder with sample app  
RUN mkdir -p /webdir && rm -fr /var/www/html && ln -s /webdir /var/www/html  
RUN git clone https://github.com/CodeForEindhoven/buurtpreventie.git /webdir  
  
EXPOSE 80  
WORKDIR /webdir  
COPY parameters.yml /webdir/app/config/parameters.yml  
  
# config to enable .htaccess  
COPY apache2.conf /etc/apache2/apache2.conf  
RUN a2enmod rewrite  
  
CMD ["/run.sh"]  

