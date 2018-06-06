FROM crazycode/jdk7  
  
MAINTAINER crazycode  
  
ENV ACTIVEMQ_VERSION 5.10.0  
ENV ACTIVEMQ apache-activemq-$ACTIVEMQ_VERSION  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y curl && \  
apt-get -qq clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -O http://mirror2.klaus-
uwe.me/apache/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-bin.tar.gz && \  
mkdir -p /opt && \  
tar xf $ACTIVEMQ-bin.tar.gz -C /opt/ && \  
rm $ACTIVEMQ-bin.tar.gz && \  
ln -s /opt/$ACTIVEMQ /opt/activemq  
  
WORKDIR /opt/activemq  
EXPOSE 61616 8161  
CMD ["/bin/bash", "-c", "bin/activemq console"]  

