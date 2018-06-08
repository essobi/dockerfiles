FROM mustardgrain/java8:latest  
  
MAINTAINER Kirk True <kirk@mustardgrain.com>  
  
CMD ["/sbin/my_init"]  
  
ENV SPARK_VERSION 1.3.0  
ENV SPARK_URL
http://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-
bin-hadoop2.4.tgz  
ENV SPARK_HOME /opt/spark-$SPARK_VERSION-bin-hadoop2.4  
RUN cd /opt && /usr/bin/curl -L -s $SPARK_URL | tar xz  
  
COPY . /src  
  
RUN mkdir -p /etc/service/spark && cp /src/run /etc/service/spark  
  
WORKDIR $SPARK_HOME  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

