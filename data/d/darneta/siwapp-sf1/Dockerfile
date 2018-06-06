############################################################  
# Dockerfile  
############################################################  
FROM ubuntu:trusty  
  
MAINTAINER Darius Kristapavicius  
  
RUN echo "Europe/Vilnius" > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-gd \  
php5-curl \  
php5-xsl \  
mysql-client \  
mysql-common \  
php-pear \  
unzip \  
wget \  
php-apc && \  
rm -rf /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN update-rc.d -f apache2 remove  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
RUN rm -fr /var/www/html  
RUN wget https://github.com/darneta/siwapp-sf1/archive/master.zip  
RUN unzip master.zip  
RUN rm master.zip  
RUN cp -r ./siwapp-sf1-master /app  
WORKDIR /app  
COPY ./assets /app/container  
RUN ln -s /app/web /var/www/html  
  
VOLUME ["/app/web/uploads"]  
  
RUN touch mycron  
RUN echo "*/15 * * * * /usr/bin/php /app/symfony siwapp:create-pending-
invoices >/dev/null 2>&1" >> mycron  
RUN crontab mycron  
RUN rm mycron  
  
EXPOSE 80  
  
RUN chmod g+x /app/container/init  
  
ENTRYPOINT ["/app/container/init"]  

