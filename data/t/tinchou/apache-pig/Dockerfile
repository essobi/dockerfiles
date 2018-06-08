FROM java:7-jre  
MAINTAINER Martín González Coll <martingonzalezcoll@gmail.com>  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64/jre/  
ENV PIG_VERSION 0.15.0  
RUN curl -LO
http://apache.cs.utah.edu/pig/pig-$PIG_VERSION/pig-$PIG_VERSION.tar.gz  
RUN tar xzf pig-$PIG_VERSION.tar.gz  
  
ENV PATH $PATH:/pig-$PIG_VERSION/bin  
  
ADD run_pig.sh run_pig.sh  
RUN chmod +x /run_pig.sh  
  
WORKDIR /code  
  
ENTRYPOINT ["/run_pig.sh"]  

