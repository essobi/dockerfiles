FROM centos:7  
MAINTAINER Tremolo Security, Inc. - Docker <docker@tremolosecurity.com>  
EXPOSE 9090  
EXPOSE 8080  
EXPOSE 8443  
EXPOSE 9093  
ENV UNISON_VERSION 1.0.14  
ENV MYSQL_JDBC_VERSION 5.1.38  
ENV PGSQL_JDBC_VERSION 9.4.1209.jre7  
  
  
USER root  
ADD scripts/firstStart.sh /tmp/firstStart.sh  
ADD scripts/startUnisonInDocker.sh /tmp/startUnisonInDocker.sh  
ADD conf/log4j2.xml /tmp/log4j2.xml  
  
RUN yum -y install wget which java-1.8.0-openjdk-devel;cd /etc/yum.repos.d &&
\  
groupadd -r tremoloadmin -g 433 && \  
useradd -u 431 -r -g tremoloadmin -d /usr/local/tremolo/tremolo-service -s
/sbin/nologin -c "Unison Docker image user" tremoloadmin && \  
cd /tmp && \  
wget https://www.tremolosecurity.com/dwn/tremolosecurity-
downloads/unison/${UNISON_VERSION}/tremolo-service-${UNISON_VERSION}.tar.gz &&
\  
tar -xvzf tremolo-service-${UNISON_VERSION}.tar.gz && \  
mkdir -p /usr/local/tremolo/tremolo-service && \  
mv /tmp/tremolo-service-${UNISON_VERSION}/* /usr/local/tremolo/tremolo-service
&& \  
rm -rf /tmp/tremolo-service-* && \  
rm /usr/local/tremolo/tremolo-service/conf/log4j2.xml && \  
mv /tmp/log4j2.xml /usr/local/tremolo/tremolo-service/conf/log4j2.xml && \  
mkdir /tmp/drivers && \  
cd /tmp/drivers && \  
curl -L -O https://search.maven.org/remotecontent?filepath=mysql/mysql-
connector-java/${MYSQL_JDBC_VERSION}/mysql-connector-
java-${MYSQL_JDBC_VERSION}.jar && \  
curl -L -O
https://search.maven.org/remotecontent?filepath=org/postgresql/postgresql/${PGSQL_JDBC_VERSION}/postgresql-${PGSQL_JDBC_VERSION}.jar
&& \  
mkdir /usr/local/tremolo/tremolo-service/external && \  
mv /tmp/firstStart.sh /usr/local/tremolo/tremolo-service/bin/ && \  
mv /tmp/startUnisonInDocker.sh /usr/local/tremolo/tremolo-service/bin/ && \  
chmod +x /usr/local/tremolo/tremolo-service/bin/startUnisonInDocker.sh && \  
chmod +x /usr/local/tremolo/tremolo-service/bin/firstStart.sh && \  
chown -R tremoloadmin:tremoloadmin /usr/local/tremolo && \  
chmod -R ugo+rw /usr/local/tremolo && \  
chmod -R ugo+rw /tmp/drivers && \  
yum -y clean all  
  
VOLUME /usr/local/tremolo/tremolo-service/external  
  
USER 431  
WORKDIR /usr/local/tremolo/tremolo-service  
ENV JAVA_OPTS -XX:+UseParallelGC -Djava.security.egd=file:/dev/./urandom  
  
HEALTHCHECK CMD curl --insecure -v https://localhost:9090/ 2>&1 | grep subject
|| exit 1  
  
CMD /usr/local/tremolo/tremolo-service/bin/firstStart.sh  

