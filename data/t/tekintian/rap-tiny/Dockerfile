# Set the base image to centos6.8  
FROM centos:6.8  
# File Author / Maintainer  
MAINTAINER TekinTian tekintian@gmail.com  
  
# Base rpm  
RUN yum install -y vim wget crontabs gcc make git unzip && yum clean all  
  
#java-1.8.0-openjdk-headless  
RUN yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel.x86_64 && \  
yum clean all  
  
#redis  
COPY conf/redis/redis /etc/init.d/redis  
COPY conf/redis/redis.conf /etc/redis.conf  
RUN chmod +x /etc/init.d/redis && cd /usr/src && \  
wget http://download.redis.io/releases/redis-3.2.10.tar.gz && tar xzf
redis-3.2.10.tar.gz && cd redis-3.2.10 && make && \  
cp src/redis-server /usr/sbin/redis-server && cp src/redis-cli
/usr/sbin/redis-cli && \  
rm -rf /usr/src/redis-3.2.10.tar.gz  
  
#tomcat  
RUN wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-8/v8.5.20/bin/apache-
tomcat-8.5.20.tar.gz && tar xzf apache-tomcat-8.5.20.tar.gz && \  
mv ./apache-tomcat-8.5.20 /usr/local/tomcat8 && \  
sed -i "s/port=\"8080\"/port=\"80\"/g" /usr/local/tomcat8/conf/server.xml && \  
rm -rf apache-tomcat-8.5.20.tar.gz  
  
#RAP deploy START  
RUN wget http://rapapi.org/release/RAP-0.14.16-SNAPSHOT.war && \  
mv RAP-0.14.16-SNAPSHOT.war /usr/local/tomcat8/webapps/ROOT.war && \  
rm -rf /usr/local/tomcat8/webapps/ROOT  
  
# RAP deploy END  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENV PATH=/usr/local/bin:${PATH}  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["/bin/bash"]

