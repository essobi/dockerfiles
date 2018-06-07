FROM library/ubuntu:xenial-20160818  
MAINTAINER kindermoumoute@hotmail.fr  
  
ENV DATA_DIR=/data \  
BIND_USER=bind  
  
RUN rm -rf /etc/apt/apt.conf.d/docker-gzip-indexes \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y bind9 \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 8053/tcp  
VOLUME ["${DATA_DIR}"]  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["/usr/sbin/named"]  

