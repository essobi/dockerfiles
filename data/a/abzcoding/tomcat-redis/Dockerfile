# This tag use tomcat 8 alongside jre 8  
FROM tomcat:jre8  
  
MAINTAINER Abouzar Parvan <abzcoding@gmail.com>  
  
ENV REDIS_HOST redis  
ENV REDIS_PORT 6379  
RUN \  
cd /usr/local/tomcat/lib && \  
wget -q
http://central.maven.org/maven2/redis/clients/jedis/2.8.1/jedis-2.8.1.jar && \  
wget -q http://central.maven.org/maven2/org/apache/commons/commons-
pool2/2.4.2/commons-pool2-2.4.2.jar  
  
# used https://github.com/pivotalsoftware/session-managers.git  
COPY redis-store-1.3.0.BUILD-SNAPSHOT.jar /usr/local/tomcat/lib/redis-
store-1.3.0.BUILD-SNAPSHOT.jar  
  
# optional  
COPY setenv.sh /usr/local/tomcat/bin/setenv.sh  
RUN chmod +x /usr/local/tomcat/bin/setenv.sh  
  
# remove all default applications  
RUN rm -rf /usr/local/tomcat/webapps/*  
  
# set session manager to redis  
COPY run-with-redis.sh /run-with-redis.sh  
COPY run.sh /run.sh  
RUN chmod +x /*.sh  
CMD ["/run-with-redis.sh"]  

