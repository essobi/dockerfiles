FROM java:7  
MAINTAINER Elton Stoneman <elton@sixeyed.com>  
  
ENV JAVA_HOME=/usr  
ENV SCALA_HOME=/usr/lib/scala  
ENV PATH=$PATH:/usr/lib/scala/bin:/usr/lib/spark/bin  
  
RUN mkdir /setup  
WORKDIR /setup  
  
ADD install-spark.sh /setup/  
RUN ./install-spark.sh  
  
ADD log4j.properties /usr/lib/spark/conf  
  
WORKDIR /usr/lib/spark  
  
CMD /usr/lib/spark/bin/spark-shell

