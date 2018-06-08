FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
apache2 \  
php5 php5-mysql && \  
apt-get clean  
  
# Clean Apache configuration  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
  
# Fix apache logs  
#RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log &&  
# ln -sf /proc/self/fd/1 /var/log/apache2/error.log  
  
EXPOSE 80  
  
VOLUME /www  
WORKDIR /www  
  
COPY main.sh /  
  
ENTRYPOINT ["/main.sh"]  
  

