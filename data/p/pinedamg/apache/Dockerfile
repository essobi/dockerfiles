FROM pinedamg/base  
MAINTAINER MPineda <pinedamg@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
USER root  
  
RUN apt-get update  
RUN apt-get install -y apache2  
  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
RUN a2enmod rewrite  
RUN a2enmod headers  
  
EXPOSE 80  
EXPOSE 443  
COPY ./aliases /root/aliases  
RUN cat /root/aliases >> /root/.bash_aliases && rm -f /root/aliases  
  
RUN apt-get update && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  
WORKDIR /var/www

