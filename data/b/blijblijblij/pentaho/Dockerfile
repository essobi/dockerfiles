FROM blijblijblij/java:8-alpine  
  
MAINTAINER Rogier Wessel <rhwessel@xs4all.nl>  
  
ENV MAJOR_VERSION 6.1  
ENV MINOR_VERSION 6.1.0.1-196  
ENV PENTAHO_HOME /opt/pentaho  
  
RUN apk add --update wget unzip && \  
adduser -S pentaho && \  
mkdir ${PENTAHO_HOME} && \  
echo
http://downloads.sourceforge.net/project/pentaho/Data%20Integration/${MAJOR_VERSION}/pdi-
ce-${MINOR_VERSION}.zip \  
| xargs wget -qO- -O tmp.zip && \  
unzip -q tmp.zip -d ${PENTAHO_HOME} && \  
rm -f tmp.zip && \  
wget -qO- -O ${PENTAHO_HOME}/data-integration/lib/mysql.jar
https://github.com/blijblijblij/docker/raw/develop/lib/mysql-connector-
java-5.1.35-bin.jar && \  
wget -qO- -O ${PENTAHO_HOME}/data-integration/lib/postgres.jar
https://github.com/blijblijblij/docker/raw/develop/lib/postgresql-9.4-1201.jdbc41.jar
&& \  
wget -qO- -O ${PENTAHO_HOME}/data-integration/lib/vertica.jar
https://github.com/blijblijblij/docker/raw/develop/lib/vertica-
jdbc-7.2.3-0.jar && \  
chown -R pentaho ${PENTAHO_HOME} && \  
apk del wget unzip  
  
ENTRYPOINT ["zsh"]  
  
USER pentaho  

