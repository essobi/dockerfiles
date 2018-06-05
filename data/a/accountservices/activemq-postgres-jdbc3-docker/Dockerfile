FROM java:8  
ENV ACTIVEMQ_VERSION 5.12.0  
ENV ACTIVEMQ apache-activemq-$ACTIVEMQ_VERSION  
  
RUN \  
curl -O
http://apache.mirrors.spacedump.net/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-
bin.tar.gz && \  
mkdir -p /opt && \  
tar xf $ACTIVEMQ-bin.tar.gz -C /opt/ && \  
rm $ACTIVEMQ-bin.tar.gz && \  
ln -s /opt/$ACTIVEMQ /opt/activemq && \  
cd /opt/$ACTIVEMQ/lib/optional && \  
curl -O https://jdbc.postgresql.org/download/postgresql-9.3-1102.jdbc3.jar &&
\  
rm -rf /opt/$ACTIVEMQ/conf  
  
WORKDIR /opt/activemq  
  
EXPOSE 8161  
EXPOSE 61616  
VOLUME /opt/activemq/conf  
  
CMD ["./bin/activemq", "console"]  

