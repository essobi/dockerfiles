FROM debian:jessie  
  
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys
514A2AD631A57A16DD0047EC749D6EEC0353B12C  
  
RUN echo 'deb http://www.apache.org/dist/cassandra/debian 21x main' >>
/etc/apt/sources.list.d/cassandra.list  
  
ENV CASSANDRA_VERSION 2.1.8  
RUN apt-get update \  
&& apt-get install -y cassandra="$CASSANDRA_VERSION" \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CASSANDRA_CONFIG /etc/cassandra  
  
RUN rm -f /etc/security/limits.d/cassandra.conf  
  
EXPOSE 7199 7000 7001 9160 9042 22 8012 61621  
COPY start-cassandra.sh /start-cassandra.sh  
  
ENTRYPOINT ["/start-cassandra.sh"]  

