FROM debian:jessie  
MAINTAINER Antoine Millet <antoine@inaps.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install python php5 \  
php5-sqlite php5-mcrypt php5-gd php5-curl php5-mysql \  
&& apt-get clean  
  
RUN rm -Rf /var/www/*  
  
RUN a2enmod deflate && a2enmod expires && a2enmod headers  
  
ADD launcher.py /  
RUN chmod +x /launcher.py  
  
EXPOSE 80  
VOLUME /var/www/  
  
CMD []  
ENTRYPOINT ["/launcher.py"]  

