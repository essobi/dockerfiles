FROM pinedamg/magento  
MAINTAINER MPineda <pinedamg@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#ADD MAGENTO RECOMMENDED SETTINGS  
COPY zz-magento2.ini /etc/php5/cli/conf.d/zz-magento2.ini  
COPY zz-magento2.ini /etc/php5/apache2/conf.d/zz-magento2.ini  
  
RUN apt-get update && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*

