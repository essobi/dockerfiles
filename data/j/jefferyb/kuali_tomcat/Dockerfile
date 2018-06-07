#  
# Kuali Coeus on tomcat Dockerfile  
# This docker image works with the jefferyb/kuali_db_mysql docker image...  
#  
# https://github.com/jefferyb/docker-tomcat-kuali-coeus  
#  
# To Build:  
# docker build -t jefferyb/kuali_tomcat .  
#  
# To Run:  
# docker run -d --name kuali-coeus-database -p 3306:3306
jefferyb/kuali_db_mysql  
# docker run -d --name kuali-coeus-application -e KUALI_APP_URL=EXAMPLE.COM -e
KUALI_APP_URL_PORT=8080 -e MYSQL_HOSTNAME=kuali-coeus-database --link kuali-
coeus-database -p 8080:8080 jefferyb/kuali_tomcat  
#  
# To watch the logs:  
# docker logs -f kuali-coeus-application  
# Pull base image.  
FROM ubuntu:16.04  
MAINTAINER Jeffery Bagirimvano <jeffery.rukundo@gmail.com>  
  
# MySQL Settings:  
RUN mkdir -p /setup_files  
ADD setup_files /setup_files  
ENV HOST_NAME="kuali_coeus"  
# kc-config.xml Settings:  
ENV KUALI_APP_URL="localhost"  
ENV KUALI_APP_URL_PORT="8080"  
ENV MYSQL_HOSTNAME="kuali-coeus-database"  
ENV MYSQL_PORT="3306"  
ENV MYSQL_USER="kcusername"  
ENV MYSQL_PASSWORD="kcpassword"  
ENV MYSQL_DATABASE="kualicoeusdb"  
# Tomcat Settings:  
ENV TOMCAT_LOCATION="/opt/apache-tomcat/tomcat8"  
ENV KC_CONFIG_XML_LOC="/opt/kuali/main/dev"  
# MySQL Connector Java  
ENV
MYSQL_CONNECTOR_LINK="http://mirror.cogentco.com/pub/mysql/Connector-J/mysql-
connector-java-5.1.34.zip"  
ENV MYSQL_CONNECTOR_ZIP_FILE="mysql-connector-java-5.1.34.zip"  
ENV MYSQL_CONNECTOR_FILE="mysql-connector-java-5.1.34/mysql-connector-
java-5.1.34-bin.jar"  
# Tomcat - Spring Instrumentation  
ENV
SPRING_INSTRUMENTATION_TOMCAT_LINK="http://central.maven.org/maven2/org/springframework/spring-
instrument-tomcat/3.2.13.RELEASE/spring-instrument-tomcat-3.2.13.RELEASE.jar"  
# Install Tomcat  
RUN \  
apt-get update && \  
apt-get install -y curl w3m && \  
TOMCAT_MAJOR="8" && \  
TOMCAT_VERSION="$(w3m https://tomcat.apache.org/download-80.cgi -dump | grep
"KEYS |" | sed 's/KEYS | //' | sed 's/ |.*//')" && \  
TOMCAT_LINK="https://www.apache.org/dist/tomcat/tomcat-$TOMCAT_MAJOR/v$TOMCAT_VERSION/bin/apache-
tomcat-$TOMCAT_VERSION.tar.gz" && \  
TOMCAT_FILE="apache-tomcat-${TOMCAT_VERSION}.tar.gz" && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && \  
apt-get install -y wget zip unzip oracle-java8-installer tar graphviz && \  
cd /setup_files && \  
wget ${TOMCAT_LINK} && \  
mkdir -p ${TOMCAT_LOCATION} && \  
tar --strip-components=1 -zxvf ${TOMCAT_FILE} -C ${TOMCAT_LOCATION} && \  
wget ${MYSQL_CONNECTOR_LINK} && \  
unzip -j ${MYSQL_CONNECTOR_ZIP_FILE} ${MYSQL_CONNECTOR_FILE} -d
${TOMCAT_LOCATION}/lib && \  
cp /setup_files/setenv.sh ${TOMCAT_LOCATION}/bin && \  
cd ${TOMCAT_LOCATION}/lib && \  
wget ${SPRING_INSTRUMENTATION_TOMCAT_LINK} && \  
sed -i 's/<Context>/<Context>\n <!-- END - For Kuali Coeus - Jeffery B. -->/'
${TOMCAT_LOCATION}/conf/context.xml && \  
sed -i 's/<Context>/<Context>\n <Loader
loaderClass="org.springframework.instrument.classloading.tomcat.TomcatInstrumentableClassLoader"\/>/'
${TOMCAT_LOCATION}/conf/context.xml && \  
sed -i 's/<Context>/<Context>\n\n <!-- BEGIN - For Kuali Coeus -->/'
${TOMCAT_LOCATION}/conf/context.xml && \  
mkdir -p ${KC_CONFIG_XML_LOC} && \  
cp -f /setup_files/kc-config.xml ${KC_CONFIG_XML_LOC}/kc-config.xml && \  
  
KC_VERSION="$(w3m https://raw.githubusercontent.com/kuali/kc/master/pom.xml
-dump | grep -m 1 "<version>" | sed 's/.*.<version>//' | sed 's/\\..*//')" &&
\  
KC_WAR_FILE_LINK="http://www.kuali.erafiki.com/${KC_VERSION}/mysql/kc-dev.war"
&& \  
KC_PROJECT_RICE_XML="http://www.kuali.erafiki.com/${KC_VERSION}/xml_files/rice-
xml-${KC_VERSION}.zip" && \  
KC_PROJECT_COEUS_XML="http://www.kuali.erafiki.com/${KC_VERSION}/xml_files/coeus-
xml-${KC_VERSION}.zip" && \  
  
wget ${KC_WAR_FILE_LINK} -O ${TOMCAT_LOCATION}/webapps/kc-dev.war && \  
mkdir -p ${TOMCAT_LOCATION}/webapps/ROOT/xml_files && \  
wget ${KC_PROJECT_RICE_XML} -O ${TOMCAT_LOCATION}/webapps/ROOT/xml_files/rice-
xml-$(echo ${KC_VERSION} | sed 's/coeus-//').zip && \  
wget ${KC_PROJECT_COEUS_XML} -O
${TOMCAT_LOCATION}/webapps/ROOT/xml_files/coeus-xml-$(echo ${KC_VERSION} | sed
's/coeus-//').zip && \  
rm -fr /setup_files && \  
rm -rf /var/lib/apt/lists/* && \  
echo "Done Setting Tomcat!!!"  
# Expose ports.  
EXPOSE 8080  
# Define default command.  
CMD \  
KC_VERSION="$(w3m https://raw.githubusercontent.com/kuali/kc/master/pom.xml
-dump | grep -m 1 "<version>" | sed 's/.*.<version>//' | sed 's/\\..*//')"; \  
sed -i "3 s/KUALI_APP_URL/${KUALI_APP_URL}/" ${KC_CONFIG_XML_LOC}/kc-
config.xml; \  
sed -i "4 s/KUALI_APP_URL_PORT/${KUALI_APP_URL_PORT}/"
${KC_CONFIG_XML_LOC}/kc-config.xml; \  
sed -i "s/KUALI_COEUS_VERSION/KualiCo ${KC_VERSION}/" ${KC_CONFIG_XML_LOC}/kc-
config.xml; \  
sed -i "10 s/MYSQL_HOSTNAME/${MYSQL_HOSTNAME}/" ${KC_CONFIG_XML_LOC}/kc-
config.xml; \  
sed -i "10 s/MYSQL_PORT/${MYSQL_PORT}/" ${KC_CONFIG_XML_LOC}/kc-config.xml; \  
sed -i "10 s/MYSQL_DATABASE/${MYSQL_DATABASE}/" ${KC_CONFIG_XML_LOC}/kc-
config.xml; \  
sed -i "11 s/MYSQL_USER/${MYSQL_USER}/" ${KC_CONFIG_XML_LOC}/kc-config.xml; \  
sed -i "12 s/MYSQL_PASSWORD/${MYSQL_PASSWORD}/" ${KC_CONFIG_XML_LOC}/kc-
config.xml; \  
service mysql restart; \  
${TOMCAT_LOCATION}/bin/startup.sh; \  
tailf ${TOMCAT_LOCATION}/logs/catalina.out  

