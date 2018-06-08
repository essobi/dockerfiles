FROM pinedamg/apache  
MAINTAINER MPineda <pinedamg@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
#INSTALL PHP AND EXTENSIONS  
RUN apt-get update  
RUN apt-get -y install php5 \  
php5-cli php5-mysql \  
php5-gd php5-imagick \  
php5-mcrypt php-soap \  
php5-xsl php5-memcached \  
php5-imap php5-xdebug \  
php5-curl php5-json  
  
RUN php5enmod mcrypt  
  
#CONFIG PHPXDEBUG  
RUN echo "xdebug.remote_host=192.168.0.100" >>
/etc/php5/cli/conf.d/20-xdebug.ini  
RUN echo "xdebug.idekey=phpstorm" >> /etc/php5/cli/conf.d/20-xdebug.ini  
RUN echo "xdebug.remote_enable=On" >> /etc/php5/cli/conf.d/20-xdebug.ini  
RUN echo "xdebug.remote_connect_back=On" >> /etc/php5/cli/conf.d/20-xdebug.ini  
  
RUN apt-get update && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#INSTALL CRON  
RUN apt-get update && apt-get install -y cron rsyslog  
RUN apt-get update && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#INSTALL SENDMAIL  
RUN apt-get update && apt-get install -y sendmail-bin  
ADD sendmail.sh /root/bin/sendmail.sh  
RUN echo "sh /root/bin/sendmail.sh &> /dev/null" >> /root/.bashrc  
  
#INSTALL MYSQL CLIENT  
RUN apt-get update && apt-get install -y mysql-client  
  
#ADD ALIASES  
COPY ./aliases /root/aliases  
RUN cat /root/aliases >> /root/.bash_aliases && rm -f /root/aliases  
  
RUN apt-get update && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*RUN apt-get update && apt-get -y
autoremove && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

