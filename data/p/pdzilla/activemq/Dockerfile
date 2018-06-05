FROM java:7-jdk  
MAINTAINER Patrick Davis <patrick_davis@cable.comcast.com>  
  
#some variables to make it more generic, etc.  
ENV ACTIVEMQ_VERSION=5.8.0  
ENV ACTIVEMQ=apache-activemq-$ACTIVEMQ_VERSION  
ENV ACTIVEMQ_ROOT="/usr/local"  
ENV ACTIVEMQ_HOME="$ACTIVEMQ_ROOT/$ACTIVEMQ"  
ENV ACTIVEMQ_CONF="$ACTIVEMQ_HOME/conf"  
ENV PATH=$ACTIVEMQ_HOME/bin:$PATH  
  
RUN mkdir -p "$ACTIVEMQ_HOME"  
  
WORKDIR $ACTIVEMQ_HOME  
RUN curl -O http://archive.apache.org/dist/activemq/apache-
activemq/$ACTIVEMQ_VERSION/$ACTIVEMQ-bin.tar.gz \  
&& tar -xzmf $ACTIVEMQ-bin.tar.gz -C $ACTIVEMQ_ROOT \  
&& rm -f $ACTIVEMQ-bin.tar.gz  
  
EXPOSE 61612 61613 61616 8161  
CMD $ACTIVEMQ_HOME/bin/activemq console

