FROM xabufr/java:8  
ENV ACTIVEMQ_VERSION 5.11.2  
ENV ACTIVEMQ apache-activemq-$ACTIVEMQ_VERSION  
  
ENV ACTIVEMQ_HOME /opt/activemq  
  
RUN \  
curl -O http://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-
bin.tar.gz && \  
mkdir -p /opt && \  
tar xf $ACTIVEMQ-bin.tar.gz -C /opt/ && \  
rm $ACTIVEMQ-bin.tar.gz && \  
mv /opt/$ACTIVEMQ $ACTIVEMQ_HOME; \  
mkdir -p /etc/service/activemq  
  
ADD activemq.sh /etc/service/activemq/run  
  
EXPOSE 8161  
EXPOSE 61616  
EXPOSE 5672  
EXPOSE 61613  
EXPOSE 1883  
EXPOSE 61614  
CMD ["/sbin/my_init"]  

