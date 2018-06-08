FROM enricomariam42/baseimage-java8:latest  
LABEL maintainer="Enrico Maria Carmona, e.carmona@asst-monza.it"  
  
ENV PDI_HOME=/opt/pentaho/data-integration \  
KETTLE_HOME=/data-integration  
  
ENV PATH=${PDI_HOME}:${PATH}  
  
ENV BASE_REL=7.1 \  
REV=0.9-96 \  
GDRIVE_FILE_ID=1dvTqrzRXicoZ9k33cPMXu8PnnrZLIxqI  
  
RUN apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -f -y -q \  
unzip \  
zip  
  
RUN mkdir /opt/pentaho && \  
# curl -L -o /tmp/pdi-ce-${BASE_REL}.${REV}.zip \  
#
http://sourceforge.net/projects/pentaho/files/Data%20Integration/${BASE_REL}/pdi-
ce-${BASE_REL}.${REV}.zip/download && \  
curl -L https://github.com/circulosmeos/gdown.pl/raw/master/gdown.pl -o
gdown.pl && \  
perl gdown.pl https://drive.google.com/file/d/${GDRIVE_FILE_ID}/edit /tmp/pdi-
ce-${BASE_REL}.${REV}.zip && \  
unzip -q /tmp/pdi-ce-${BASE_REL}.${REV}.zip -d /opt/pentaho && \  
rm /tmp/pdi-ce-${BASE_REL}.${REV}.zip && \  
rm gdown.pl  
  
# speed up https://blog.twineworks.com/improving-startup-time-of-pentaho-data-
integration-78d0803c559b  
RUN cd /opt/pentaho/data-integration && \  
rm -rfv \  
classes/kettle-lifecycle-listeners.xml \  
classes/kettle-registry-extensions.xml \  
lib/pdi-engine-api-*.jar \  
lib/pdi-engine-spark-*.jar \  
lib/pdi-osgi-bridge-core-*.jar \  
lib/pdi-spark-driver-*.jar \  
lib/pentaho-capability-manager-*.jar \  
lib/pentaho-connections-*.jar \  
lib/pentaho-cwm-*.jar \  
lib/pentaho-database-model-*.jar \  
lib/pentaho-hadoop-shims-api-*.jar \  
lib/pentaho-metaverse-api-*.jar \  
lib/pentaho-osgi-utils-api-*.jar \  
lib/pentaho-platform-api-*.jar \  
lib/pentaho-platform-core-*.jar \  
lib/pentaho-platform-extensions-*.jar \  
lib/pentaho-platform-repository-*.jar \  
lib/pentaho-service-coordinator-*.jar \  
plugins/kettle5-log4j-plugin \  
plugins/*-xml-plugin \  
plugins/pentaho-big-data-plugin \  
system/karaf \  
system/mondrian \  
system/osgi  
  
# update jdbc drivers  
RUN rm -f ${PDI_HOME}/lib/postgresql-* \  
${PDI_HOME}/lib/monetdb-jdbc* && \  
# monetdb  
MONETDB_JDBC_VERSION=`curl -s https://clojars.org/repo/monetdb/monetdb-
jdbc/maven-metadata.xml | grep -Po '<release>.*' | grep -Po [0-9\\.]+` && \  
wget -O ${PDI_HOME}/lib/monetdb-jdbc-${MONETDB_JDBC_VERSION}.jar
https://clojars.org/repo/monetdb/monetdb-jdbc/${MONETDB_JDBC_VERSION}/monetdb-
jdbc-${MONETDB_JDBC_VERSION}.jar && \  
# mysql  
MYSQL_JDBC_VERSION=`curl -s https://repo1.maven.org/maven2/mysql/mysql-
connector-java/maven-metadata.xml | grep -Po '<version>5.1.*' | grep -Po
[0-9\\.]+ | head -1` && \  
wget -O ${PDI_HOME}/lib/mysql-connector-java-${MYSQL_JDBC_VERSION}.jar
https://search.maven.org/remotecontent?filepath=mysql/mysql-connector-
java/${MYSQL_JDBC_VERSION}/mysql-connector-java-${MYSQL_JDBC_VERSION}.jar && \  
# postgres  
POSTGRES_JDBC_VERSION=`curl -s
'https://search.maven.org/solrsearch/select?q=a:%22postgresql%22+AND+g:%22org.postgresql%22&wt=json'
| grep -Po '"latestVersion":"[0-9.a-z]+' | grep -Pow '[0-9\\.\\-a-z]+'` && \  
wget -O ${PDI_HOME}/lib/postgresql-${POSTGRES_JDBC_VERSION}.jar
https://search.maven.org/remotecontent?filepath=org/postgresql/postgresql/${POSTGRES_JDBC_VERSION}/postgresql-${POSTGRES_JDBC_VERSION}.jar  
  
# copy oracle jdbc driver  
COPY oracle/ojdbc7.jar ${PDI_HOME}/lib/  
  
RUN mkdir -p ${KETTLE_HOME}/.kettle /docker-entrypoint.d /templates && \  
echo "KETTLE_SYSTEM_HOSTNAME=localhost" >> /data-
integration/.kettle/kettle.properties  
  
COPY carte_config*.xml /templates/  
  
COPY docker-entrypoint.sh /  
  
EXPOSE 8080  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["carte.sh", "/data-integration/carte_config.xml"]  
  

