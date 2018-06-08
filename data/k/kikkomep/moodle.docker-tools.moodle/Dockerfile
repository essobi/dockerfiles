FROM ubuntu:14.04  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update  
RUN apt-get update  
  
# Install Apache/MySQL/PHP  
RUN apt-get -y install apache2 mysql-client php5 git-core  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
# Install Additional Software  
RUN apt-get -y install graphviz aspell php5-pspell php5-curl php5-gd php5-intl
php5-mysql php5-xmlrpc php5-ldap clamav  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php5/apache2/php.ini  
  
# Path of the apache WWW root  
ENV WWW_ROOT /var/www/html  
  
### Moodle Download and Setting ###  
# Moodle Env  
ENV MOODLE_VERSION MOODLE_29_STABLE  
ENV MOODLE_WWW_ROOT ${WWW_ROOT}/moodle  
ENV MOODLE_DATA_DIR /data/moodle  
  
# Clone Moodle  
RUN cd /opt \  
&& git clone https://github.com/moodle/moodle.git \  
&& cd moodle \  
&& git checkout ${MOODLE_VERSION}  
  
# Init Moodle dirs  
RUN mkdir -p ${MOODLE_DATA_DIR}  
RUN chown -R www-data ${MOODLE_DATA_DIR}  
RUN chmod -R 777 ${MOODLE_DATA_DIR}  
  
### Global scripts ###  
ADD scripts/start-services.sh /usr/local/bin/start-services  
RUN chmod +x /usr/local/bin/start-services  
  
### PORTS to expose ###  
EXPOSE 80  
### ENTRYPOINT ##  
CMD ["start-services"]

