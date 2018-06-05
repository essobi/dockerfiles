FROM objectstyle/java8:latest  
  
MAINTAINER Andrus Adamchik <andrus at objectstyle dot com>  
  
LABEL name=objectstyle-activemq  
  
ENV ACTIVEMQ_VERSION 5.12.1  
ENV ACTIVEMQ apache-activemq-$ACTIVEMQ_VERSION  
  
ENV ACTIVEMQ_HOME /opt/activemq  
  
RUN \  
curl -O http://archive.apache.org/dist/activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-
bin.tar.gz \  
&& mkdir -p /opt \  
&& tar xf $ACTIVEMQ-bin.tar.gz -C /opt/ \  
&& rm $ACTIVEMQ-bin.tar.gz \  
&& ln -s /opt/$ACTIVEMQ $ACTIVEMQ_HOME  
  
WORKDIR $ACTIVEMQ_HOME  
  
CMD ["/bin/bash", "-c", "bin/activemq console"]

