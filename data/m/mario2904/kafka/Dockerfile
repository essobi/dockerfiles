FROM ubuntu:14.04  
WORKDIR /root  
  
RUN apt-get update && apt-get install -y software-properties-common wget  
  
# Install Oracle's Java  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle  
RUN add-apt-repository -y ppa:webupd8team/java && apt-get update && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| debconf-set-selections && \  
apt-get install -y oracle-java8-installer  
  
ENV SCALA_VERSION=2.12  
ENV KAFKA_VERSION=0.10.2.0  
ENV KAFKA_HOME=/usr/local/kafka  
ENV PATH=$PATH:$KAFKA_HOME/bin  
RUN wget http://www-
us.apache.org/dist/kafka/$KAFKA_VERSION/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz
&& \  
tar xzf kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz && \  
mv kafka_$SCALA_VERSION-$KAFKA_VERSION $KAFKA_HOME && \  
rm kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz  
  
COPY scripts/* /usr/bin/  
RUN chmod a+x /usr/bin/init-kafka.sh  

