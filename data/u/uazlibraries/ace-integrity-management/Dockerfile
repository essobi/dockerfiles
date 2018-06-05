FROM payara/server-full:5.181  
  
ENV ACE_V=1.12 MAVEN_V=3.5.3 MAVEN=apache-maven-3.5.3 MYSQL_JCONNECT_V=5.1.46
MYSQL_JCONNECT=mysql-connector-java-5.1.46 J2EE_INIT_SLEEP=40  
  
RUN \  
mkdir -p /opt/ace-ims && \  
mkdir -p build && cd build && \  
curl -kL https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-$MYSQL_JCONNECT_V.tar.gz | tar xz && \  
cp $MYSQL_JCONNECT/$MYSQL_JCONNECT-bin.jar ../glassfish/domains/domain1/lib &&
\  
curl -kL http://apache.claz.org/maven/maven-3/$MAVEN_V/binaries/$MAVEN-
bin.tar.gz | tar xz && \  
git clone -b ace-$ACE_V https://gitlab.umiacs.umd.edu/adapt/ace.git && \  
cd ace && ../$MAVEN/bin/mvn package && \  
cp ace-ims-ear/target/ace-ims.ear ../../deployments && \  
cd ../.. && rm -fr build && rm -fr .m2  
  
COPY docker/* /opt/ace-ims/  
  
ENTRYPOINT [ `ls -1A deployments | wc -l` -eq 0 ] &&
${PAYARA_PATH}/bin/asadmin start-domain -v ${PAYARA_DOMAIN} || ( /opt/ace-
ims/setup.sh && ${PAYARA_PATH}/bin/asadmin start-domain -v ${PAYARA_DOMAIN} )  

