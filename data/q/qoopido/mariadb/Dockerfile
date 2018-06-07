FROM qoopido/base:1.0.3  
MAINTAINER Dirk Lüth <info@qoopido.com>  
  
# Initialize environment  
CMD ["/sbin/my_init"]  
ENV DEBIAN_FRONTEND noninteractive  
  
# configure defaults  
COPY configure.sh /  
ADD config /config  
RUN chmod +x /configure.sh \  
&& chmod 755 /configure.sh  
RUN /configure.sh && \  
chmod +x /etc/my_init.d/*.sh \  
&& chmod 755 /etc/my_init.d/*.sh \  
&& chmod +x /etc/service/mariadb/run \  
&& chmod 755 /etc/service/mariadb/run  
  
# install packages  
RUN apt-get update \  
&& apt-get install -qy mariadb-server  
  
# add default /app directory  
RUN mkdir -p /app/data/logs \  
&& mkdir -p /app/data/database \  
&& mkdir -p /app/config  
  
# cleanup  
RUN apt-get -qy autoremove \  
&& deborphan | xargs apt-get -qy remove --purge \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/* /usr/share/doc/*
/usr/share/man/* /tmp/* /var/tmp/* /configure.sh \  
&& find /var/log -type f -name '*.gz' -exec rm {} + \  
&& find /var/log -type f -exec truncate -s 0 {} +  
  
# finalize  
VOLUME ["/app/data", "/app/config"]  
EXPOSE 3306  

