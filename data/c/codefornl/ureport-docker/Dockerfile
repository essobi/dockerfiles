FROM ubuntu:trusty  
MAINTAINER Milo van der Linden <milo@dogodigi.net>  
  
# Install base packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
curl \  
git \  
gettext \  
imagemagick \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-intl \  
php5-curl \  
php-pear \  
php-apc && \  
rm -rf /var/lib/apt/lists/* &&\  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN /usr/sbin/php5enmod mcrypt  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \  
sed -i "s/variables_order.*/variables_order = \"EGPCS\"/g"
/etc/php5/apache2/php.ini  
  
#Defaults, modify with environment variable to change  
ENV ALLOW_OVERRIDE **False**  
ENV APPLICATION_NAME CRM  
ENV LOCATION_NAME City of Bloomington, Mark Kruzan, Mayor  
ENV APPLICATION_THEME local  
ENV BASE_URI /crm  
ENV ADMINISTRATOR_NAME Site Admin  
ENV ADMINISTRATOR_EMAIL admin@servername.com  
ENV DB_HOST localhost  
ENV DB_NAME open311  
ENV DB_USER root  
ENV DB_PASS password  
ENV DATE_FORMAT n/j/Y H:i:s  
ENV NOTIFICATIONS_ENABLED true  
ENV SOLR_SERVER_HOSTNAME localhost  
ENV SOLR_SERVER_PORT 8983  
ENV SOLR_SERVER_PATH /solr/crm  
ENV SOLR_CORE crm  
ENV DEFAULT_CITY Bloomington  
ENV DEFAULT_STATE IN  
ENV OPEN311_JURISDICTION localhost  
ENV OPEN311_KEY_SERVICE http://localhost/open311-api-key-request  
ENV THUMBNAIL_SIZE 150  
ENV CLOSING_COMMENT_REQUIRED_LENGTH 1  
ENV AUTO_CLOSE_COMMENT Closed automatically  
ENV LOCALE en_US  
  
  
# Add image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
# Configure /webdir folder with sample app  
RUN mkdir -p /webdir  
RUN git clone \--branch bootstrap-version --recursive
https://github.com/CodeForEindhoven/uReport.git /webdir  
RUN ln -s /webdir/crm /var/www/html/crm  
EXPOSE 80  
WORKDIR /webdir/crm  
RUN composer install --prefer-source --no-interaction  
  
WORKDIR /webdir  
COPY configuration.inc /webdir/crm/configuration.inc  
COPY site_config.inc /webdir/crm/data/site_config.inc  
COPY default /etc/apache2/sites-available/default  
COPY solr5.sh /webdir/solr5.sh  
COPY schema.json /webdir/schema.json  
  
CMD ["/run.sh"]  

