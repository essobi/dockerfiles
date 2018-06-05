FROM ibandrea/jdk-oracle:8u121  
MAINTAINER Andrea Lorenzetti <andrea@ibuildings.it>  
  
ENV BAMBOO_VERSION 5.15.2  
ENV MYSQL_CONNECTOR_JAVA_VERSION 5.1.40  
ENV BAMBOO_HOME /var/local/atlassian/bamboo  
ENV BAMBOO_INSTALL /usr/local/atlassian/bamboo  
ENV BAMBOO_USER bamboo  
ENV BAMBOO_INSTALLER atlassian-bamboo-$BAMBOO_VERSION.tar.gz  
  
RUN deps=" \  
libtcnative-1 libapr1 libaprutil1 \  
xmlstarlet \  
wget \  
" \  
set -x && \  
export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get upgrade -y $deps \--no-install-recommends && \  
\  
useradd --create-home --shell /bin/bash $BAMBOO_USER && \  
\  
cd /tmp && \  
wget --no-check-certificate
http://www.atlassian.com/software/bamboo/downloads/binary/$BAMBOO_INSTALLER &&
\  
mkdir -p $BAMBOO_INSTALL && \  
tar zxf $BAMBOO_INSTALLER \--strip=1 -C $BAMBOO_INSTALL && \  
mkdir -p $BAMBOO_HOME && \  
echo -e "\nbamboo.home=$BAMBOO_HOME" >> "$BAMBOO_INSTALL/atlassian-bamboo/WEB-
INF/classes/bamboo-init.properties" && \  
\  
wget --no-check-certificate
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-$MYSQL_CONNECTOR_JAVA_VERSION.tar.gz && \  
tar xzf mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION.tar.gz -C /tmp && \  
cp /tmp/mysql-connector-java-$MYSQL_CONNECTOR_JAVA_VERSION/mysql-connector-
java-$MYSQL_CONNECTOR_JAVA_VERSION-bin.jar $BAMBOO_INSTALL/lib/ && \  
\  
chown -R $BAMBOO_USER:$BAMBOO_USER $BAMBOO_HOME && \  
chown -R $BAMBOO_USER:$BAMBOO_USER $BAMBOO_INSTALL && \  
\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/var/local/atlassian/bamboo"]  
  
EXPOSE 8085  
EXPOSE 54663  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
COPY start-bamboo.sh /start-bamboo.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["/start-bamboo.sh"]  

