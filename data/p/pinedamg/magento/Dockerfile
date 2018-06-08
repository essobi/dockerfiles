FROM pinedamg/apache-php  
MAINTAINER MPineda <pinedamg@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#INSTALL MAGERUN  
RUN apt-get update && apt-get -y install wget  
RUN wget https://files.magerun.net/n98-magerun.phar  
RUN chmod +x ./n98-magerun.phar  
  
#ADD MAGERUN ALIAS  
RUN mv ./n98-magerun.phar /usr/local/bin/magerun  
RUN chmod +x /usr/local/bin/magerun  
  
#ADD MAGERUN ALIASES  
COPY ./aliases /root/aliases  
RUN cat /root/aliases >> /root/.bash_aliases && rm -f /root/aliases  
  
#ADD MAGENTO RECOMMENDED SETTINGS  
COPY zz-magento.ini /etc/php5/cli/conf.d/zz-magento.ini  
COPY zz-magento.ini /etc/php5/apache2/conf.d/zz-magento.ini  
  
#ADD VIRTUALHOST  
COPY vhost.conf /etc/apache2/sites-enabled/000-default.conf  
COPY vhost.conf /etc/apache2/sites-available/000-default.conf  
  
RUN apt-get update && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  

