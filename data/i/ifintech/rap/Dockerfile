############################################################  
# 带ssh的centos  
# Based on Centos 6.8  
#  
############################################################  
# Set the base image to centos6.8  
FROM centos:6.8  
  
# File Author / Maintainer  
MAINTAINER lvyalin lvyalin.yl@gmail.com  
  
##################### 常用基础软件 START #####################  
RUN yum install -y vsftpd vim wget crontabs gcc make openssh-server git unzip
&& yum clean all  
##################### 常用基础软件 END #####################  
  
##################### 安装java-1.8.0-openjdk-headless #########  
RUN yum install -y java-1.8.0-openjdk && \  
yum install -y java-1.8.0-openjdk-devel.x86_64 && \  
yum clean all  
##################### 安装java-1.8.0-openjdk-headless end #####  
  
###################### redis START #####################  
COPY conf/redis/redis /etc/init.d/redis  
COPY conf/redis/redis.conf /etc/redis.conf  
RUN chmod +x /etc/init.d/redis && cd /usr/src && \  
wget http://download.redis.io/releases/redis-3.2.9.tar.gz && tar xzf
redis-3.2.9.tar.gz && cd redis-3.2.9 && make && \  
cp src/redis-server /usr/sbin/redis-server && cp src/redis-cli
/usr/sbin/redis-cli && \  
rm -rf /usr/src/redis-3.2.9.tar.gz  
###################### redis END #####################  
  
###################### mysql START #####################  
RUN rpm -Uvh https://dev.mysql.com/get/mysql57-community-release-
el6-9.noarch.rpm && \  
yum -y install mysql-community-server && \  
yum clean all  
###################### mysql END #####################  
  
###################### tomcat START ############################  
RUN wget http://mirror.bit.edu.cn/apache/tomcat/tomcat-8/v8.5.20/bin/apache-
tomcat-8.5.20.tar.gz && tar xzf apache-tomcat-8.5.20.tar.gz && \  
mv ./apache-tomcat-8.5.20 /usr/local/apache-tomcat && \  
sed -i "s/port=\"8080\"/port=\"80\"/g" /usr/local/apache-
tomcat/conf/server.xml && \  
rm -f /apache-tomcat-8.5.20.tar.gz  
###################### tomcat END #################################  
  
###################### RAP deploy START ############################  
RUN wget http://rapapi.org/release/RAP-0.14.16-SNAPSHOT.war && \  
mv RAP-0.14.16-SNAPSHOT.war /usr/local/apache-tomcat/webapps/ROOT.war && \  
rm -rf /usr/local/apache-tomcat/webapps/ROOT  
###################### RAP deploy END ############################  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
CMD ["/bin/bash"]

