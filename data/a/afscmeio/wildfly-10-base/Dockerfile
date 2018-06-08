FROM afscmeio/java-8-base:latest  
MAINTAINER AFSCME DevOps <devops@afscme.io>  
#  
# add additional software first  
#  
RUN yum -y update \  
&& yum -y install libaio \  
&& yum -y clean all  
  
#  
# environment  
#  
ENV WILDFLY_VERSION=10.1.0.Final \  
WILDFLY_SHA1=9ee3c0255e2e6007d502223916cefad2a1a5e333 \  
WILDFLY_UID=1000 \  
WILDFLY_USER=jboss \  
WILDFLY_DEPLOY_BASE=/var/lib/jboss \  
MODULE_XML=module.xml  
#  
ENV WILDFLY_FILE=wildfly-${WILDFLY_VERSION}.tar.gz \  
WILDFLY_USER_HOME=/opt/${WILDFLY_USER}"  
#  
ENV WILDFLY_HOME=${WILDFLY_USER_HOME}/wildfly \  
WILDFLY_MGMT_USER=admin \  
WILDFLY_MGMT_PSWD=wildfly \  
WILDFLY_MODULE_XML=/tmp/module.xml \  
WILDFLY_MODULE_BASE=modules/system/layers/base  
#  
# jdbc jar constants  
#  
ENV JDBCLDAP_JAR_VER=2.1 \  
JTDS_JAR_VER=1.3.1 \  
MYSQL_JAR_VER=5.1.39 \  
PGSQL_JAR_VER=9.4.1209 \  
SQLITE_JAR_VER=3.8.11.2  
#  
# jtds  
#  
ENV JTDS_JAR_BASE=jtds \  
JTDS_JAR_PATH=net/sourceforge/jtds \  
JTDS_MODULE_PATH=net/sourceforge/jtds/jdbc/main \  
JTDS_MODULE_NAME=net.sourceforge.jtds.jdbc  
#  
ENV JTDS_JAR_FILE=${JTDS_JAR_BASE}-${JTDS_JAR_VER}.jar \  
JTDS_JAR_ANON=${JTDS_JAR_BASE}.jar \  
JTDS_MODULE_HOME=${WILDFLY_HOME}/${WILDFLY_MODULE_BASE}/${JTDS_MODULE_PATH}  
#  
ENV
JTDS_JAR_LINK="http://search.maven.org/remotecontent?filepath=${JTDS_JAR_PATH}/${JTDS_JAR_BASE}/${JTDS_JAR_VER}/${JTDS_JAR_FILE}"  
#  
# mysql  
#  
ENV MYSQL_JAR_BASE=mysql \  
MYSQL_JAR_PATH=mysql/mysql-connector-java \  
MYSQL_MODULE_PATH=com/mysql/jdbc/main \  
MYSQL_MODULE_NAME=com.mysql.jdbc  
#  
ENV MYSQL_JAR_FILE=${MYSQL_JAR_BASE}-connector-java-${MYSQL_JAR_VER}.jar \  
MYSQL_JAR_ANON=${MYSQL_JAR_BASE}.jar \  
MYSQL_MODULE_HOME=${WILDFLY_HOME}/${WILDFLY_MODULE_BASE}/${MYSQL_MODULE_PATH}  
#  
ENV
MYSQL_JAR_LINK="http://search.maven.org/remotecontent?filepath=${MYSQL_JAR_PATH}/${MYSQL_JAR_VER}/${MYSQL_JAR_FILE}"  
#  
# postgresql  
#  
ENV PGSQL_JAR_BASE=postgresql \  
PGSQL_JAR_PATH=org/postgresql \  
PGSQL_MODULE_PATH=org/postgresql/jdbc/main \  
PGSQL_MODULE_NAME=org.postgresql.jdbc  
#  
ENV PGSQL_JAR_FILE=${PGSQL_JAR_BASE}-${PGSQL_JAR_VER}.jar \  
PGSQL_JAR_ANON=${PGSQL_JAR_BASE}.jar \  
PGSQL_MODULE_HOME=${WILDFLY_HOME}/${WILDFLY_MODULE_BASE}/${PGSQL_MODULE_PATH}  
#  
ENV
PGSQL_JAR_LINK="http://search.maven.org/remotecontent?filepath=${PGSQL_JAR_PATH}/${PGSQL_JAR_BASE}/${PGSQL_JAR_VER}/${PGSQL_JAR_FILE}"  
#  
# sqlite  
#  
ENV SQLITE_JAR_BASE=sqlite \  
SQLITE_JAR_PATH=org/xerial/sqlite-jdbc \  
SQLITE_MODULE_PATH=org/sqlite/jdbc/main \  
SQLITE_MODULE_NAME=org.sqlite.jdbc  
#  
ENV SQLITE_JAR_FILE=${SQLITE_JAR_BASE}-jdbc-${SQLITE_JAR_VER}.jar \  
SQLITE_JAR_ANON=${SQLITE_JAR_BASE}.jar \  
SQLITE_MODULE_HOME=${WILDFLY_HOME}/${WILDFLY_MODULE_BASE}/${SQLITE_MODULE_PATH}  
#  
ENV
SQLITE_JAR_LINK="http://search.maven.org/remotecontent?filepath=${SQLITE_JAR_PATH}/${SQLITE_JAR_VER}/${SQLITE_JAR_FILE}"  
#  
# jdbc-ldap  
#  
ENV JDBCLDAP_JAR_BASE=jdbc-ldap \  
JDBCLDAP_JAR_PATH=jdbc%20ldap%20bridge \  
JDBCLDAP_JAR_ANON=jdbcLdap.jar \  
LDAP_JAR_ANON=ldap.jar \  
JDBCLDAP_MODULE_PATH=com/octetstring/jdbcLdap/main \  
JDBCLDAP_MODULE_NAME=com.octetstring.jdbcLdap  
#  
ENV JDBCLDAP_JAR_TAG=${JDBCLDAP_JAR_BASE}-${JDBCLDAP_JAR_VER} \  
JDBCLDAP_JAR_FILE=jdbcLdap-${JDBCLDAP_JAR_VER}.jar \  
LDAP_JAR_TAG=ldap-${JDBCLDAP_JAR_VER} \  
JDBCLDAP_JAR_PATH_VER=${JDBCLDAP_JAR_PATH}%20${JDBCLDAP_JAR_VER} \  
JDBCLDAP_MODULE_HOME=${WILDFLY_HOME}/${WILDFLY_MODULE_BASE}/${JDBCLDAP_MODULE_PATH}  
#  
ENV JDBCLDAP_ARCHIVE=${JDBCLDAP_JAR_TAG}.tar.gz \  
LDAP_JAR_FILE=${LDAP_JAR_TAG}.jar  
#  
ENV
JDBCLDAP_JAR_LINK="https://sourceforge.net/projects/myvd/files/${JDBCLDAP_JAR_PATH}/${JDBCLDAP_JAR_PATH_VER}/${JDBCLDAP_ARCHIVE}/download"  
  
RUN echo -e " " \  
&& echo -e " WILDFLY_VERSION=[${WILDFLY_VERSION}]" \  
&& echo -e " WILDFLY_SHA1=[${WILDFLY_SHA1}]" \  
&& echo -e " WILDFLY_UID=[${WILDFLY_UID}]" \  
&& echo -e " WILDFLY_USER=[${WILDFLY_USER}]" \  
&& echo -e "WILDFLY_DEPLOY_BASE=[${WILDFLY_DEPLOY_BASE}]" \  
&& echo -e " WILDFLY_FILE=[${WILDFLY_FILE}]" \  
&& echo -e " WILDFLY_USER_HOME=[${WILDFLY_USER_HOME}]" \  
&& echo -e " WILDFLY_HOME=[${WILDFLY_HOME}]" \  
&& echo -e " "  
# Create a user and group to launch wildfly  
# The user ID 1000 is the default for the first "regular" user on
Fedora/RHEL/CentOS,  
# so there is a high chance that this ID will be equal to the current user  
# making it easier to use volumes (no permission issues)  
RUN groupadd -r "${WILDFLY_USER}" -g "${WILDFLY_UID}" \  
&& useradd -u "${WILDFLY_UID}" -r -g "${WILDFLY_USER}" -m -d
"${WILDFLY_USER_HOME}" -s /sbin/nologin -c "Wildfly user" "${WILDFLY_USER}" \  
&& chmod 755 "${WILDFLY_USER_HOME}"  
#  
# fetch and unpack wildfly, purge remnants, create external mount point  
#  
RUN cd "${WILDFLY_USER_HOME}" \  
&& curl --silent -O
https://download.jboss.org/wildfly/"${WILDFLY_VERSION}"/"${WILDFLY_FILE}" \  
&& sha1sum "${WILDFLY_FILE}" | grep "${WILDFLY_SHA1}" \  
&& tar zxf "${WILDFLY_FILE}" \  
&& mv wildfly-"${WILDFLY_VERSION}" "${WILDFLY_HOME}" \  
&& rm "${WILDFLY_FILE}" \  
&& mkdir -p "${WILDFLY_DEPLOY_BASE}/standalone/deploy" \  
&& mkdir -p "${WILDFLY_DEPLOY_BASE}/standalone/undeploy" \  
&& mkdir -p "${WILDFLY_DEPLOY_BASE}/domain/deploy" \  
&& mkdir -p "${WILDFLY_DEPLOY_BASE}/domain/undeploy"  
#  
# create ${WILDFLY_HOME}/wildfly.properties  
#  
RUN echo -e "##########################################" >
${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "# commonly customized wildfly properties #" >>
${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "##########################################" >>
${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "jboss.bind.address=0.0.0.0" >> ${WILDFLY_HOME}/wildfly.properties
\  
&& echo -e "jboss.bind.address.management=0.0.0.0" >>
${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "#jboss.socket.binding.port-offset=0" >>
${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "#jboss.management.http.port=9990" >>
${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "#jboss.management.https.port=9993" >>
${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "#jboss.ajp.port=8009" >> ${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "#jboss.http.port=8080" >> ${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "#jboss.https.port=8443" >> ${WILDFLY_HOME}/wildfly.properties \  
&& echo -e "###########################" >> ${WILDFLY_HOME}/wildfly.properties
\  
&& echo -e "# custom properties below #" >> ${WILDFLY_HOME}/wildfly.properties
\  
&& echo -e "###########################" >> ${WILDFLY_HOME}/wildfly.properties  
  
#  
# create ${WILDFLY_USER_HOME}/clean-wildfly  
#  
RUN echo -e "#!/bin/sh\n#\nwildfly/bin/clean-wildfly.sh \"\$@\"" >
${WILDFLY_USER_HOME}/clean-wildfly \  
&& chmod +x ${WILDFLY_USER_HOME}/clean-wildfly  
  
#  
# create base module.xml ${WILDFLY_MODULE_XML}  
#  
RUN echo -e "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" >
${WILDFLY_MODULE_XML} \  
&& echo -e "<module xmlns=\"urn:jboss:module:1.3\" name=\"MODULE_NAME\">" >>
${WILDFLY_MODULE_XML} \  
&& echo -e " <resources>" >> ${WILDFLY_MODULE_XML} \  
&& echo -e " <resource-root path=\"MODULE_JAR\"/>" >> ${WILDFLY_MODULE_XML} \  
&& echo -e " <!-- Insert resources here -->" >> ${WILDFLY_MODULE_XML} \  
&& echo -e " </resources>" >> ${WILDFLY_MODULE_XML} \  
&& echo -e " <dependencies>" >> ${WILDFLY_MODULE_XML} \  
&& echo -e " <module name=\"javax.api\"/>" >> ${WILDFLY_MODULE_XML} \  
&& echo -e " <module name=\"javax.transaction.api\"/>" >>
${WILDFLY_MODULE_XML} \  
&& echo -e " </dependencies>" >> ${WILDFLY_MODULE_XML} \  
&& echo -e "</module>" >> ${WILDFLY_MODULE_XML}  
  
#  
# jtds  
#  
RUN mkdir -p ${JTDS_MODULE_HOME} \  
&& curl --silent --location --retry 5 \  
"${JTDS_JAR_LINK}" -o "${JTDS_MODULE_HOME}/${JTDS_JAR_FILE}" \  
&& cp -a ${WILDFLY_MODULE_XML} ${JTDS_MODULE_HOME}/ \  
&& sed -ri "s#MODULE_NAME#${JTDS_MODULE_NAME}#g"
${JTDS_MODULE_HOME}/${MODULE_XML} \  
&& sed -ri "s#MODULE_JAR#${JTDS_JAR_FILE}#g" ${JTDS_MODULE_HOME}/${MODULE_XML}  
  
#  
# mysql  
#  
RUN mkdir -p ${MYSQL_MODULE_HOME} \  
&& curl --silent --location --retry 5 \  
"${MYSQL_JAR_LINK}" -o "${MYSQL_MODULE_HOME}/${MYSQL_JAR_FILE}" \  
&& cp -a ${WILDFLY_MODULE_XML} ${MYSQL_MODULE_HOME}/ \  
&& sed -ri "s#MODULE_NAME#${MYSQL_MODULE_NAME}#g"
${MYSQL_MODULE_HOME}/${MODULE_XML} \  
&& sed -ri "s#MODULE_JAR#${MYSQL_JAR_FILE}#g"
${MYSQL_MODULE_HOME}/${MODULE_XML}  
  
#  
# postgresql  
#  
RUN mkdir -p ${PGSQL_MODULE_HOME} \  
&& curl --silent --location --retry 5 \  
"${PGSQL_JAR_LINK}" -o "${PGSQL_MODULE_HOME}/${PGSQL_JAR_FILE}" \  
&& cp -a ${WILDFLY_MODULE_XML} ${PGSQL_MODULE_HOME}/ \  
&& sed -ri "s#MODULE_NAME#${PGSQL_MODULE_NAME}#g"
${PGSQL_MODULE_HOME}/${MODULE_XML} \  
&& sed -ri "s#MODULE_JAR#${PGSQL_JAR_FILE}#g"
${PGSQL_MODULE_HOME}/${MODULE_XML}  
  
#  
# sqlite  
#  
RUN mkdir -p ${SQLITE_MODULE_HOME} \  
&& curl --silent --location --retry 5 \  
"${SQLITE_JAR_LINK}" -o "${SQLITE_MODULE_HOME}/${SQLITE_JAR_FILE}" \  
&& cp -a ${WILDFLY_MODULE_XML} ${SQLITE_MODULE_HOME}/ \  
&& sed -ri "s#MODULE_NAME#${SQLITE_MODULE_NAME}#g"
${SQLITE_MODULE_HOME}/${MODULE_XML} \  
&& sed -ri "s#MODULE_JAR#${SQLITE_JAR_FILE}#g"
${SQLITE_MODULE_HOME}/${MODULE_XML}  
  
#  
# jdbc-ldap  
#  
RUN mkdir -p ${JDBCLDAP_MODULE_HOME} \  
&& curl --silent --location --retry 5 \  
"${JDBCLDAP_JAR_LINK}" -o "/tmp/${JDBCLDAP_ARCHIVE}" \  
&& tar -zxf "/tmp/${JDBCLDAP_ARCHIVE}" -C "/tmp/" \  
&& cp -a "/tmp/${JDBCLDAP_JAR_TAG}/${JDBCLDAP_JAR_ANON}"
"${JDBCLDAP_MODULE_HOME}/${JDBCLDAP_JAR_FILE}" \  
&& cp -a "/tmp/${JDBCLDAP_JAR_TAG}/${LDAP_JAR_ANON}"
"${JDBCLDAP_MODULE_HOME}/${LDAP_JAR_FILE}" \  
&& cp -a ${WILDFLY_MODULE_XML} ${JDBCLDAP_MODULE_HOME}/ \  
&& sed -ri "s#MODULE_NAME#${JDBCLDAP_MODULE_NAME}#g"
${JDBCLDAP_MODULE_HOME}/${MODULE_XML} \  
&& sed -ri "s#MODULE_JAR#${JDBCLDAP_JAR_FILE}\"/>\n <resource-root
path=\"${LDAP_JAR_FILE}#g" ${JDBCLDAP_MODULE_HOME}/${MODULE_XML}  
  
#  
# TODO choose starting cfg file from startup with a -e parameter  
# copy and customize configuration:  
#  
# tune loggers  
# add jdbc drivers  
# add logging formatters  
# add ssl cipher restrictions  
#  
# add host mapped deployment folder  
# add listener attributes  
# add ajp listener  
# adjust logging formatters  
#  
COPY xml /tmp/  
RUN cp -a ${WILDFLY_HOME}/standalone/configuration/standalone-full.xml \  
${WILDFLY_HOME}/standalone/configuration/standalone-custom.xml  
#  
RUN sed -i -e '/<root-logger>/{ r /tmp/loggers.xml' -e 'd}'
${WILDFLY_HOME}/standalone/configuration/standalone-custom.xml \  
&& sed -i -e '/<drivers>/{ r /tmp/drivers.xml' -e 'd}'
${WILDFLY_HOME}/standalone/configuration/standalone-custom.xml \  
&& sed -i -e '/<formatter name=\"PATTERN\">/{ r /tmp/logging-formatters.xml'
-e 'd}' ${WILDFLY_HOME}/standalone/configuration/standalone-custom.xml \  
&& sed -i -e '/<ssl>/{ r /tmp/ssl-ciphers.xml' -e 'd}'
${WILDFLY_HOME}/standalone/configuration/standalone-custom.xml  
#  
RUN sed -ri 's#(deployment-scanner path[^>]+>)#\1\n <deployment-scanner
name="custom" path="/var/lib/jboss/standalone/deploy" scan-enabled="true"
scan-interval="5000" deployment-timeout="120"/>#g'
${WILDFLY_HOME}/standalone/configuration/standalone-custom.xml \  
&& sed -ri 's#(<http-listener name=\"default\")#\1 max-parameters="2000" max-
post-size="104857600"#g' ${WILDFLY_HOME}/standalone/configuration/standalone-
custom.xml \  
&& sed -ri 's#(<https-listener name=\"https\")#\1 max-parameters="2000" max-
post-size="104857600"#g' ${WILDFLY_HOME}/standalone/configuration/standalone-
custom.xml \  
&& sed -ri 's#(<server name=\"default-server\">)#\1\n <ajp-listener name="ajp"
max-parameters="2000" max-post-size="104857600" socket-binding="ajp"
scheme="ajp"/>\n#g' ${WILDFLY_HOME}/standalone/configuration/standalone-
custom.xml  
#  
RUN sed -ri 's#(<named-formatter name=\")(COLOR-PATTERN\")#\1CUSTOM-\2#g'
${WILDFLY_HOME}/standalone/configuration/standalone-custom.xml \  
&& sed -ri 's#(<named-formatter name=\")(PATTERN\")#\1CUSTOM-\2#g'
${WILDFLY_HOME}/standalone/configuration/standalone-custom.xml  
  
#  
# copy customizations  
#  
COPY bin "${WILDFLY_HOME}"/bin/  
  
#  
# set permissions after all copies  
#  
RUN chown -R jboss.jboss "${WILDFLY_USER_HOME}" \  
&& chown -R jboss.jboss "${WILDFLY_DEPLOY_BASE}" \  
&& chmod -R 775 "${WILDFLY_DEPLOY_BASE}"  
#  
# create a user for the management console  
#  
RUN ${WILDFLY_HOME}/bin/add-user.sh -u ${WILDFLY_MGMT_USER} -p
${WILDFLY_MGMT_PSWD}  
  
#  
# make a JBOSS_HOME snippet  
#  
RUN echo -e "#!/bin/sh\n#\nexport JBOSS_HOME=${WILDFLY_HOME}\n" >
/etc/profile.d/wildfly.sh  
  
#  
# mark the external deployment folder as a volume  
#  
VOLUME "${WILDFLY_DEPLOY_BASE}"  
#  
# Set the working directory to wildfly user home directory  
#  
WORKDIR "${WILDFLY_USER_HOME}"  
#  
# Specify the user which should be used to execute all commands below  
#  
USER "${WILDFLY_USER}"  
# Ensure signals are forwarded to the JVM process correctly for graceful
shutdown  
ENV LAUNCH_JBOSS_IN_BACKGROUND true  
  
# expose default http and management ports only  
EXPOSE 8080 9990  
  
CMD ["/opt/jboss/wildfly/bin/standalone.sh", "-c", "standalone-custom.xml",
"-P", "/opt/jboss/wildfly/wildfly.properties"]  

