FROM excelmicro/base:v1.0.0  
MAINTAINER Ani Channarasappa <achannarasappa@excelmicro.com>  
  
RUN apt-get update && apt-get install -y python-software-properties  
  
RUN add-apt-repository -y ppa:ondrej/php5-5.6  
  
RUN apt-get update && apt-get install -y --force-yes \  
supervisor \  
apache2 \  
php5 \  
curl \  
libcurl3 \  
libcurl3-dev \  
php5-curl \  
php5-pgsql \  
php5-sybase \  
freetds-dev \  
libapache2-mod-php5 \  
php-apc \  
git  
  
ADD start-apache2.sh /start-apache2.sh  
ADD run.sh /run.sh  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
RUN chmod 755 /*.sh  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
RUN mkdir -p /app && rm -fr /var/www && ln -s /app /var/www  
ONBUILD ADD . /app  
  
EXPOSE 80  
CMD ["/run.sh"]  

