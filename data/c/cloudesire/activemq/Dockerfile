FROM cloudesire/java:7  
ENV ACTIVEMQ_VERSION 5.13.0  
ENV ACTIVEMQ apache-activemq-$ACTIVEMQ_VERSION  
  
ENV ACTIVEMQ_HOME /opt/activemq  
  
RUN \  
apt-get update && \  
apt-get install -y wget && \  
wget -nv http://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-
bin.tar.gz && \  
apt-get remove -y --purge wget && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists && \  
mkdir -p /opt && \  
tar xf $ACTIVEMQ-bin.tar.gz -C /opt/ && \  
rm $ACTIVEMQ-bin.tar.gz && \  
ln -s /opt/$ACTIVEMQ $ACTIVEMQ_HOME  
  
WORKDIR $ACTIVEMQ_HOME  
EXPOSE 61616 8161  
COPY ./activemq.sh /  
  
ENTRYPOINT ["/activemq.sh"]  

