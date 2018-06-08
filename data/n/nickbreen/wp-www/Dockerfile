FROM phusion/baseimage:0.10.1  
LABEL maintainer="nick@foobar.net.nz"  
  
RUN apt-get update -qqy \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qqy \  
apache2 \  
apache2-utils \  
&& apt-get clean -qqy  
  
# Configure a service entry for Apache  
RUN mkdir /etc/service/apache/  
COPY run /etc/service/apache/run  
  
COPY log.conf /etc/apache2/conf-available/log.conf  
  
RUN a2enconf log \  
&& a2disconf other-vhosts-access-log \  
&& a2enmod cache cache_disk cache_socache socache_memcache socache_shmcb dir
expires headers setenvif proxy_http proxy_fcgi rewrite  
  
RUN /etc/service/apache/run -t 2>&1  
  
EXPOSE 80  

