FROM tomcat:8.5-jre8  
  
ENV ACE_V=1.12 ACE_AUDIT_TAR=ace-am-1.12-RELEASE MYSQL_JCONNECT_V=5.1.46
MYSQL_JCONNECT=mysql-connector-java-5.1.46  
  
RUN \  
cd /opt && \  
curl -kL https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-$MYSQL_JCONNECT_V.tar.gz | tar xz && \  
cp $MYSQL_JCONNECT/$MYSQL_JCONNECT-bin.jar $CATALINA_HOME/lib && \  
curl -kL https://obj.umiacs.umd.edu/ace/releases/$ACE_V/ace-dist-$ACE_V-
RELEASE-bin.tar.gz | tar xz && \  
mkdir -p $CATALINA_HOME/conf/Catalina/localhost && \  
mkdir -p /opt/ace-am && \  
mkdir /opt/initdb.d && \  
cp $ACE_AUDIT_TAR/ace-am.sql /opt/initdb.d && \  
sed -i -e "s|MyISAM|InnoDB|g" /opt/initdb.d/ace-am.sql  
  
COPY docker/* /opt/ace-am/  
  
VOLUME ["/opt/initdb.d"]  
  
CMD [ -d "$CATALINA_HOME/webapps/ace-am" ] && catalina.sh run || ( /opt/ace-
am/setup.sh && catalina.sh run)  

