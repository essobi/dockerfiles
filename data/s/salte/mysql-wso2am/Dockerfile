FROM mysql:latest  
  
RUN apt-get update && \  
apt-get install -y zip && \  
apt-get install -y wget && \  
apt-get clean  
RUN wget --no-check-certificate -P /tmp
https://nexus.salte.io:8443/repository/wso2/api/2.1.0/platform.zip && \  
unzip /tmp/platform.zip -d /tmp  
RUN cd /docker-entrypoint-initdb.d && \  
touch apimgtdb.sql && \  
echo "SET @@GLOBAL.innodb_strict_mode='OFF';" >> apimgtdb.sql && \  
echo "SET @@GLOBAL.sql_mode='';" >> apimgtdb.sql && \  
echo "SET @@SESSION.innodb_strict_mode='OFF';" >> apimgtdb.sql && \  
echo "SET @@SESSION.sql_mode='';" >> apimgtdb.sql && \  
echo "create database apimgtdb;" >> apimgtdb.sql && \  
echo "use apimgtdb;" >> apimgtdb.sql && \  
cat /tmp/wso2am-2.1.0/dbscripts/apimgt/mysql.sql >> apimgtdb.sql && \  
echo "grant all privileges on apimgtdb.* to 'apimgr'@'%';" >> apimgtdb.sql &&
\  
echo "flush privileges;" >> apimgtdb.sql && \  
touch userdb.sql && \  
echo "SET @@GLOBAL.innodb_strict_mode='OFF';" >> userdb.sql && \  
echo "SET @@GLOBAL.sql_mode='';" >> userdb.sql && \  
echo "SET @@SESSION.innodb_strict_mode='OFF';" >> userdb.sql && \  
echo "SET @@SESSION.sql_mode='';" >> userdb.sql && \  
echo "create database userdb;" >> userdb.sql && \  
echo "use userdb;" >> userdb.sql && \  
cat /tmp/wso2am-2.1.0/dbscripts/mysql.sql >> userdb.sql && \  
echo "grant all privileges on userdb.* to 'apimgr'@'%';" >> userdb.sql && \  
echo "flush privileges;" >> userdb.sql && \  
touch regdb.sql && \  
echo "SET @@GLOBAL.innodb_strict_mode='OFF';" >> regdb.sql && \  
echo "SET @@GLOBAL.sql_mode='';" >> regdb.sql && \  
echo "SET @@SESSION.innodb_strict_mode='OFF';" >> regdb.sql && \  
echo "SET @@SESSION.sql_mode='';" >> regdb.sql && \  
echo "create database regdb;" >> regdb.sql && \  
echo "use regdb;" >> regdb.sql && \  
cat /tmp/wso2am-2.1.0/dbscripts/mysql.sql >> regdb.sql && \  
echo "grant all privileges on regdb.* to 'apimgr'@'%';" >> regdb.sql && \  
echo "flush privileges;" >> regdb.sql && \  
rm -r /tmp/wso2am-2.1.0 && \  
rm /tmp/platform.zip  
RUN wget -P /opt https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/5.0.7/flyway-commandline-5.0.7-linux-x64.tar.gz && \  
cd /opt && \  
tar -xvf flyway-commandline-5.0.7-linux-x64.tar.gz && \  
rm flyway-commandline-5.0.7-linux-x64.tar.gz  
  
ENV PATH $PATH:/opt/flyway-5.0.7  

