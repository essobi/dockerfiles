FROM alpine  
  
MAINTAINER Nicolas Lorin <androw95220@gmail.com>  
  
RUN apk add --update openjdk8-jre curl bash && rm -rf /var/cache/apk/*  
  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-2.1.1-bin-hadoop2.7.tgz
| tar -xz -C /usr/local/ && curl -s http://www-
us.apache.org/dist/zeppelin/zeppelin-0.7.1/zeppelin-0.7.1-bin-all.tgz | tar
-xz -C /usr/local/  
  
RUN cd /usr/local && ln -s spark-2.1.1-bin-hadoop2.7 spark && ln -s
zeppelin-0.7.1-bin-all zeppelin  
  
ADD scripts/*.sh /  
ADD scripts/spark-defaults.conf /spark-defaults.conf  
  
ENV SPARK_HOME /usr/local/spark  
  
EXPOSE 8080 8081  
CMD ["/start-zeppelin.sh"]  

