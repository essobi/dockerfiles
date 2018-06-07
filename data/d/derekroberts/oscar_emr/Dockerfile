# Dockerfile for the PDC's Customized OSCAR 12 service  
#  
# Steps: https://github.com/scoophealth/SCOOP-doc/wiki/OSCAR-Setup-Guide  
#  
# Ubuntu 14.04 LTS (Trusty)  
#  
FROM ubuntu:trusty  
MAINTAINER derek.roberts@gmail.com  
  
  
# Tomcat6 environment variables  
#  
ENV JAVA_HOME="/usr/lib/jvm/java-6-oracle"  
ENV CATALINA_HOME="/usr/share/tomcat6"  
ENV CATALINA_BASE="/var/lib/tomcat6"  
ENV ANT_HOME="/usr/share/ant"  
# SQL database details  
#  
ENV PASSWORD=superInsecure  
ENV DATABASE=oscar_12_1  
ENV OSCAR_PROPERTIES=${CATALINA_HOME}/oscar12.properties  
  
  
# OSCAR E2E config details  
#  
# Use differential E2E export (on/off), # of days?  
ENV E2E_DIFF=off  
ENV E2E_DIFF_DAYS=14  
#  
# Target for export (CONTAINER:PORT, no http(s): or /s)  
ENV E2E_TARGET=gateway:3001  
# Update system, add repo and install packages  
#  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo 'Dpkg::Options{ "--force-confdef"; "--force-confold" }' \  
>> /etc/apt/apt.conf.d/local; \  
echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main' \  
>> /etc/apt/sources.list.d/webupd8team-java-trusty.list; \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886; \  
echo oracle-java6-installer shared/accepted-oracle-license-v1-1 \  
select true | /usr/bin/debconf-set-selections  
RUN apt-get update; \  
apt-get install -y \  
git \  
libmysql-java \  
maven \  
mysql-server \  
oracle-java6-installer \  
runit \  
tomcat6; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# ~/.bashrc variables  
#  
RUN ( \  
echo ""; \  
echo ""; \  
echo "CATALINA_HOME="${CATALINA_HOME}; \  
echo "CATALINA_BASE="${CATALINA_BASE}; \  
echo "ANT_HOME="${ANT_HOME}; \  
echo "JAVA_HOME="${JAVA_HOME}; \  
echo "export JAVA_HOME CATALINA_HOME CATALINA_BASE ANT_HOME"; \  
) \  
>> ${HOME}/.bashrc  
  
# Clone and prep source (remove validateXml from jspc.xml)  
#  
WORKDIR /app/  
RUN git clone git://github.com/scoophealth/oscar.git -b scoop-deploy
--depth=50; \  
git clone
git://oscarmcmaster.git.sourceforge.net/gitroot/oscarmcmaster/oscar_documents;
\  
sed -i 's/validateXml="false"//' oscar/jspc.xml  
  
# Compile and deploy  
#  
WORKDIR /app/oscar/  
RUN mvn clean; \  
mvn -Dmaven.test.skip=true package; \  
cp ./target/oscar-SNAPSHOT.war ${CATALINA_BASE}/webapps/oscar12.war; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Compile and deploy  
#  
WORKDIR /app/oscar_documents/  
RUN mvn clean; \  
mvn -Dmaven.test.skip=true clean package; \  
cp ./target/oscar_documents-SNAPSHOT.war
${CATALINA_BASE}/webapps/OscarDocument.war; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Configure oscar12 properties  
#  
RUN cp /app/oscar/src/main/resources/oscar_mcmaster.properties
${OSCAR_PROPERTIES}; \  
sed -i \  
-e "s/^#*db_username *=.*/db_username = root/" \  
-e "s/^#*db_name *=.*/db_name = ${DATABASE}\?zeroDateTimeBehavior=round&useOldAliasMetadataBehavior=true&jdbcCompliantTruncation=false/" \  
-e "s/^#*db_password *=.*/db_password=${PASSWORD}/" \  
-e "s/^#*CASEMANAGEMENT *=.*/CASEMANAGEMENT = all/" \  
-e "s/^#*DOCUMENT_DIR *=.*/DOCUMENT_DIR = \/var\/lib\/tomcat6\/webapps\/OscarDocument\/oscar_mcmaster\/document\//" \  
-e "s/^#*eform_image *=.*/eform_image = \/var\/lib\/tomcat6\/webapps\/OscarDocument\/oscar_mcmaster\/eform\/images/" \  
-e "s/^#*TMP_DIR *:.*/TMP_DIR: \/var\/lib\/tomcat6\/webapps\/OscarDocument\/oscar_mcmaster\/export\//" \  
${OSCAR_PROPERTIES}  
  
# Configure oscar12 properties - BC only  
#  
RUN sed -i \  
-e "s/^#*visitlocation *=.*/visitlocation = 00|VANCOUVER/" \  
-e "s/^#*dataCenterId *=.*/dataCenterId = 00000/" \  
-e "s/^#*billregion *=.*/billregion = BC/" \  
-e "s/^#*NEW_BC_TELEPLAN *=.*/NEW_BC_TELEPLAN = yes/" \  
-e "s/^#*CDM_ALERTS *=.*/CDM_ALERTS = 250,428,4280/" \  
-e "s/^#*COUNSELING_CODES *=.*/COUNSELING_CODES = 18220,18120,17220,17120,16220,16120,13220,12220,12120,00120/" \  
-e "s/^#*phoneprefix *=.*/phoneprefix = 250-/" \  
-e "s/^#*HL7TEXT_LABS *=.*/HL7TEXT_LABS = yes/" \  
${OSCAR_PROPERTIES}  
  
# Configure oscar12 properties - E2E export  
#  
RUN sed -i \  
-e "s/^#*program *=.*/program = off/" ${OSCAR_PROPERTIES} \  
-e "s/^#*ModuleNames *= *E2E/ModuleNames = E2E/" \  
-e "s/^#*E2E_URL *=.*/E2E_URL = http:\/\/${E2E_TARGET}\/records\/create/" \  
-e "s/^#*E2E_DIFF *=.*/E2E_DIFF = ${E2E_DIFF}/" \  
-e "s/^#*E2E_DIFF_DAYS *=.*/E2E_DIFF_DAYS = ${E2E_DIFF_DAYS}/" \  
${OSCAR_PROPERTIES}  
  
# Change servlet-api.jar to tomcat-coyote.jar in catalina-tasks.xml  
#  
RUN sed -i 's/servlet-api.jar/tomcat-coyote.jar/'
${CATALINA_HOME}/bin/catalina-tasks.xml  
  
# Point Tomcat to $JAVA_HOME  
#  
RUN ( \  
echo ""; \  
echo "JAVA_HOME="${JAVA_HOME}; \  
) \  
>> /etc/default/tomcat6  
  
# MySQL - set pw, create db, .JAR classpath and base value for issue table  
#  
WORKDIR /app/oscar/database/mysql/  
RUN service mysql start; \  
mysqladmin -u root password ${PASSWORD}; \  
./createdatabase_bc.sh root ${PASSWORD} ${DATABASE}  
  
# Point oscar.properties to drugref  
#  
RUN sed -i "s/^#*drugref_url
*=.*/drugref_url=http:\/\/localhost:8080\/drugref\/DrugrefService/"
${OSCAR_PROPERTIES}  
  
# Import DrugRef Web ARchive  
#  
WORKDIR /${CATALINA_BASE}/webapps/  
RUN wget http://drugref2.googlecode.com/files/drugref.war  
  
# Create drugref.properties  
#  
RUN DRUGREF_PROPERTIES=${CATALINA_HOME}/drugref.properties; \  
( \  
echo "db_user=root"; \  
echo "db_password="${PASSWORD}; \  
echo "db_url=jdbc:mysql://127.0.0.1:3306/drugref"; \  
echo "db_driver=com.mysql.jdbc.Driver"; \  
) \  
>> ${DRUGREF_PROPERTIES}  
  
# Create database  
#  
RUN service mysql start; \  
mysql --user=root --password=${PASSWORD} -e "CREATE DATABASE drugref;"  
  
# Startup script  
#  
RUN SRV=oscar_e2e; \  
mkdir -p /etc/service/${SRV}/; \  
( \  
echo "#!/bin/bash"; \  
echo ""; \  
echo ""; \  
echo "# Start MySql"; \  
echo "#"; \  
echo "service mysql start"; \  
echo ""; \  
echo ""; \  
echo "# Import and remove any .SQL dumps"; \  
echo "#"; \  
echo "mkdir -p /e2e/"; \  
echo "cd /e2e/"; \  
echo 'find . -name "*.sql" | \'; \  
echo "while read IN"; \  
echo "do"; \  
echo ' mysql --user=root --password=${PASSWORD} ${DATABASE} < "${IN}"'; \  
echo ' rm -rf "${IN}"'; \  
echo ' echo $(date +"%Y-%m-%d")-${IN} >> import.list'; \  
echo "done"; \  
echo ""; \  
echo ""; \  
echo "# Start Tomcat6"; \  
echo "#"; \  
echo "mkdir -p /tmp/tomcat6-tomcat6-tmp/ \\\"; \  
echo " /usr/share/tomcat6/server/classes/ \\\"; \  
echo " /usr/share/tomcat6/shared/classes/"; \  
echo "exec chpst -u tomcat6:tomcat6 /usr/lib/jvm/java-6-oracle/bin/java \\\";
\  
echo "
-Djava.util.logging.config.file=/var/lib/tomcat6/conf/logging.properties \\\";
\  
echo " -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager \\\";
\  
echo " -Djava.awt.headless=true -Xmx1024m -Xms1024m -XX:MaxPermSize=512m
-server \\\"; \  
echo " -Djava.endorsed.dirs=/usr/share/tomcat6/endorsed -classpath
/usr/share/tomcat6/bin/bootstrap.jar \\\"; \  
echo " -Dcatalina.base=/var/lib/tomcat6 -Dcatalina.home=/usr/share/tomcat6
\\\"; \  
echo " -Djava.io.tmpdir=/tmp/tomcat6-tomcat6-tmp
org.apache.catalina.startup.Bootstrap start"; \  
) \  
>> /etc/service/${SRV}/run; \  
chmod +x /etc/service/${SRV}/run  
  
# Start using the script from earlier  
#  
ENTRYPOINT ["/etc/service/oscar_e2e/run"]  

