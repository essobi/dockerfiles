FROM alpine  
  
RUN apk --no-cache add bash openjdk8-jre python2  
ADD https://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-hadoop2.7.tgz
/spark/  
RUN cd /spark && tar xzf spark-2.2.0-bin-hadoop2.7.tgz  
ENV PATH=$PATH:/spark/spark-2.2.0-bin-hadoop2.7/bin  

