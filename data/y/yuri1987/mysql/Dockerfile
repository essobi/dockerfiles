FROM debian:jessie-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV GOSU_VERSION 1.7  
RUN groupadd -r mysql && useradd -r -g mysql mysql \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget mysql-server \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$(dpkg
--print-architecture)" \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apt-get purge -y --auto-remove ca-certificates wget \  
&& apt-get autoremove && apt-get autoclean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY my.cnf /etc/mysql/conf.d/my.cnf  
  
COPY run.sh /usr/local/bin/run.sh  
  
VOLUME ["/var/lib/mysql"]  
CMD ["/usr/local/bin/run.sh"]  

