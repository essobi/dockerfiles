FROM debian:wheezy  
MAINTAINER https://github.com/muccg  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get -y install --no-install-recommends \  
apache2 \  
ca-certificates \  
mysql-client \  
wget \  
supervisor \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget --quiet -O - http://packages.icinga.org/icinga.key | apt-key add -  
RUN echo "deb http://packages.icinga.org/debian icinga-wheezy-snapshots main"
>> /etc/apt/sources.list  
RUN apt-get update \  
&& apt-get -y install \  
icingaweb2 \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY supervisord/supervisord-icingaweb2.conf
/etc/supervisor/conf.d/supervisord-icingaweb2.conf  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 80 443  
VOLUME [ '/etc/icingaweb2', '/var/log/apache2' ]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD "supervisord"  

