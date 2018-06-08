# Run Spoon in container and display in a remote desktop with Xpra  
FROM enricomariam42/x11-xpra:latest  
LABEL maintainer="Enrico Maria Carmona, e.carmona@asst-monza.it"  
# java-8-oracle  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
OPT=-Doracle.jdbc.timezoneAsRegion=false  
  
RUN add-apt-repository ppa:webupd8team/java -y && \  
apt-get -qq update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
DEBIAN_FRONTEND=noninteractive apt-get install -f -y -q \  
oracle-java8-installer \  
# WebKit  
libwebkitgtk-1.0-0  
# pentaho data-integration  
ENV PDI_HOME=/opt/pentaho/data-integration \  
KETTLE_HOME=/home/user \  
PATH=/opt/pentaho/data-integration:${PATH} \  
BASE_REL=7.1 \  
REV=0.9-96 \  
GDRIVE_FILE_ID=1dvTqrzRXicoZ9k33cPMXu8PnnrZLIxqI  
  
RUN mkdir -p /opt/pentaho && \  
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
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

