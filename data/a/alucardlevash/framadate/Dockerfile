FROM debian:wheezy  
MAINTAINER Pierre Brun <pbrun.pro+github@gmail.com>  
  
ENV RELEASE wheezy  
ENV DEBIAN_FRONTEND noninteractive  
ENV SHELL /bin/bash  
  
RUN apt-get update;apt-get -y upgrade  
  
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for
debugging the container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php5 php5-mysql php5-gd php-pear php-apc php5-curl curl php5-adodb php-gettext
git mysql-client  
  
# Enable apache mods.  
RUN a2enmod php5;a2enmod rewrite  
  
RUN rm -rf /var/www; git clone https://github.com/framasoft/framadate.git
/var/www  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php5/apache2/php.ini  
  
COPY scripts/run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 80  
CMD ["/run.sh"]

