FROM debian:jessie  
  
ENV REDIS_VERSION 3.2.1  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list \  
&& apt-key adv --keyserver keys.gnupg.net --recv-keys 89DF5277 \  
&& apt-get update && apt-get install -y redis-server=2:3.2.1-1~dotdeb+8.1 \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 6379  

