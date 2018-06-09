FROM debian:testing  
MAINTAINER martin scharm  
  
# doing all in once to get rid of the useless stuff  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
apache2 \  
&& a2enmod dav_fs \  
&& a2enmod dav \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/* /var/cache/*  
  
RUN echo ErrorLog /dev/stderr >> /etc/apache2/apache2.conf \  
&& echo TransferLog /dev/stdout >> /etc/apache2/apache2.conf  
  
VOLUME ["/dav", "/acme"]  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apachectl"]  
CMD ["-d", "/etc/apache2", "-f", "/etc/apache2/apache2.conf", "-DFOREGROUND",
"-e", "info"]  

