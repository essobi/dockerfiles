FROM polinux/centos7:latest  
MAINTAINER Przemyslaw Ozgo <linux@ozgo.info>  
  
ADD install /data/install/  
  
RUN yum update -y && \  
yum install -y --nogpgcheck tar wget mariadb java-1.7.0-openjdk && \  
yum clean all && \  
cd /data/install && \  
./install.sh && \  
mv /data/install/mysql-connector-java-5.1.31-bin.jar
/opt/atlassian/confluence/confluence/WEB-INF/lib/mysql-connector-
java-5.1.31-bin.jar  
  
ADD supervisord.conf /etc/supervisord.d/confluence.conf  
EXPOSE 8090  

