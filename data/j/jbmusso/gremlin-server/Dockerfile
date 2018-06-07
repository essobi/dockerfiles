FROM openjdk:8u131-jre  
  
LABEL maintainer "jbmusso@gmail.com"  
  
ENV GREMLIN_SERVER_VERSION 3.2.4  
ENV GREMLIN_SERVER_ZIP_URL
https://www.apache.org/dyn/closer.cgi?action=download&filename=tinkerpop/$GREMLIN_SERVER_VERSION/apache-
tinkerpop-gremlin-server-$GREMLIN_SERVER_VERSION-bin.zip  
  
RUN cd /opt && \  
wget -O gremlin-server.zip "$GREMLIN_SERVER_ZIP_URL" && \  
unzip gremlin-server.zip && \  
ln -s apache-tinkerpop-gremlin-server-$GREMLIN_SERVER_VERSION gremlin-server
&& \  
rm gremlin-server.zip  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 8182  
WORKDIR /opt/gremlin-server  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["conf/gremlin-server.yaml"]  

