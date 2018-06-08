FROM java:7  
MAINTAINER Gleison Silva "geison.silva@veltio.com.com"  
ENV MYSQL_CONN_VERSION 5.1.39  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y sqlline  
  
# Download drivers  
# mysql  
RUN wget http://cdn.mysql.com//Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONN_VERSION}.tar.gz \  
-O /tmp/mysql-connector-java.tar.gz && \  
tar -xzf /tmp/mysql-connector-java.tar.gz -C /tmp && \  
cp /tmp/mysql-connector-java-${MYSQL_CONN_VERSION}/mysql-connector-
java-${MYSQL_CONN_VERSION}-bin.jar /usr/share/java/mysql-connector-java.jar &&
\  
rm -rf /tmp/mysql*  
  
# vertica  
RUN wget -c --no-check-certificate https://googledrive.com/host/0B4pi-
CIMz3h1YmgyYmRlVGJVUkE/vertica-jdbc-7.1.1-0.jar \  
-O /usr/share/java/vertica.jar  
  
# firebird  
RUN wget -c --no-check-certificate https://googledrive.com/host/0B4pi-
CIMz3h1YmgyYmRlVGJVUkE/jaybird-full-2.1.6.jar \  
-O /usr/share/java/jaybird.jar  
  
RUN sed -i 's/jtds/vertica jaybird/g' /usr/bin/sqlline  
  
CMD ["/usr/bin/sqlline"]

