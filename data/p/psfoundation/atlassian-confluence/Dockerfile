FROM psfoundation/atlassian-base:latest  
MAINTAINER Przemek Szalko <przemek@mobtitude.com>  
  
EXPOSE 8090  
  
ENV CONFLUENCE_VERSION 6.8.1  
ENV MYSQL_CONNECTOR_VERSION 5.1.46  
# CONFLUENCE Installation  
RUN DEBIAN_FRONTEND=noninteractive mkdir -p /opt/downloads && \  
mkdir -p /opt/atlassian/confluence && \  
mkdir -p /var/atlassian/application-data/confluence && \  
useradd -c "CONFLUENCE role account" -d /opt/atlassian/confluence -g atlassian
confluence && \  
wget -cnv
http://www.atlassian.com/software/confluence/downloads/binary/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz -O /opt/downloads/confluence.tar.gz &&
\  
tar -zxvf /opt/downloads/confluence.tar.gz --strip=1 -C
/opt/atlassian/confluence && \  
echo confluence.home = /var/atlassian/application-data/confluence >
/opt/atlassian/confluence/confluence/WEB-INF/classes/confluence-
init.properties && \  
sed -i "s/date +%F_%T/date +%F/" /opt/atlassian/confluence/bin/setenv.sh && \  
chown -R confluence:atlassian /opt/atlassian/confluence && chown -R
confluence:atlassian /var/atlassian/application-data/confluence && \  
  
# MYSQL connector installation  
wget -cnv http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz -O /opt/downloads/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz && \  
tar -zxvf /opt/downloads/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz -C /opt/downloads && \  
mv /opt/downloads/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}/mysql-
connector-java-${MYSQL_CONNECTOR_VERSION}-bin.jar
/opt/atlassian/confluence/confluence/WEB-INF/lib/ && \  
  
# CONFLUENCE install additional packages  
apt-get update && \  
apt-get install -y libice-dev libsm-dev libx11-dev libxext-dev libxt-dev
libxtst-dev && \  
  
# Apt clean-up  
apt-get clean autoclean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists /var/lib/cache /var/lib/log && \  
  
# Cleanup  
rm -rf /opt/downloads /opt/atlassian-home  
  
ADD server.xml /opt/atlassian/confluence/conf/server.xml  
ADD startscript.sh /usr/bin/  
  
# CONFLUENCE Start  
USER confluence  
CMD ["startscript.sh"]  

