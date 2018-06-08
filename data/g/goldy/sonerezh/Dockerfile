FROM debian:wheezy  
  
CMD ["/usr/bin/supervisord", "-n"]  
  
EXPOSE 80  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD etc /etc  
  
RUN apt-get -y update && \  
apt-get -y dist-upgrade && \  
apt-get -y install nginx php5-fpm php5-gd php5-mysql libav-tools supervisor
git  
  
RUN rm /etc/nginx/sites-enabled/default  
  
RUN mkdir /music  
VOLUME /music  
RUN chown www-data:www-data /music  
  
RUN mkdir -p /var/www/sonerezh  
RUN chown www-data:www-data /var/www/sonerezh  
USER www-data  
RUN git clone \--branch 1.0.0 https://github.com/Sonerezh/sonerezh.git
/var/www/sonerezh  
  
USER root  

