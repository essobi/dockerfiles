FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update \  
&& apt-get -y install collectd  
  
# add a fake mtab for host disk stats  
ADD etc_mtab /etc/mtab  
ADD collectd.conf.tpl /etc/collectd/collectd.conf.tpl  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["collectd", "-f"]  

