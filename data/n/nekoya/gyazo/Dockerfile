FROM ubuntu:12.04  
MAINTAINER nekoya "ryo.studiom@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "Asia/Tokyo\n" > /etc/timezone  
RUN /usr/sbin/dpkg-reconfigure -f noninteractive tzdata  
  
RUN sed -i 's/archive.ubuntu.com/ftp.jaist.ac.jp\/pub\/Linux/'
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y \  
apache2-mpm-prefork \  
ruby1.9.3  
  
# Apache2 settings  
RUN echo "ScriptAlias /gyazo/upload.cgi /opt/gyazo/upload.cgi" >
/etc/apache2/conf.d/gyazo.conf  
RUN sed -i 's/var\/www/opt\/gyazo/' /etc/apache2/sites-available/default  
  
# install Gyazo  
WORKDIR /opt/gyazo  
RUN mkdir data  
RUN mkdir db  
RUN chown -R www-data:www-data .  
COPY upload.cgi /opt/gyazo/upload.cgi  
  
EXPOSE 80  
COPY start.sh /start.sh  
CMD ["/start.sh"]  

