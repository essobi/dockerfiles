FROM ricardoamaro/uptime-base:latest  
MAINTAINER Ricardo Amaro <ricardo.amaro_at_acquia.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
RUN apt-get -y install supervisor apache2 libapache2-mod-php5 pwgen python-
setuptools \  
vim-tiny php5 php5-mysql php5-redis php-apc php5-gd php5-curl mc; \  
apt-get clean; \  
apt-get autoclean; \  
apt-get -y autoremove  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
  
# Install supervisor  
COPY ./files/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY ./files/start.sh /start.sh  
COPY ./files/foreground.sh /etc/apache2/foreground.sh  
  
RUN rm /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
enabled/*  
ADD ./files/000-default.conf /etc/apache2/sites-available/000-default.conf  
RUN a2ensite 000-default ; a2enmod rewrite vhost_alias  
  
# Display version information  
RUN php --version  
  
# Install config  
RUN mkdir /root/.ssh  
COPY ./files/config /root/.ssh/config  
RUN chmod 600 -R /root/.ssh  
  
RUN chmod 755 /start.sh /etc/apache2/foreground.sh  
WORKDIR /var/www  
EXPOSE 80  
CMD ["/bin/bash", "/start.sh"]  

