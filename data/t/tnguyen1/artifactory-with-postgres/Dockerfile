FROM java:8  
MAINTAINER Truc Nguyen <truc.nguyen@bonitasoft.com>  
  
ENV ARTIFACTORY_VERSION 4.7.6  
ENV ARTIFACTORY_SHA256
8f2ee405e7b13ea2121a0e1c97ef3097ae54e9753d7288cc4ee95d3831cb01dd  
ENV ARTIFACTORY_HOME /opt/artifactory/current  
ENV POSTGRES_JDBC_DRIVER postgresql-9.3-1102.jdbc41.jar  
ENV POSTGRES_SHA256
b78749d536da75c382d0a71c717cde6850df64e16594676fc7cacb5a74541d66  
  
RUN apt-get update \  
&& apt-get -y install net-tools postgresql-client  
  
RUN mkdir /opt/files \  
&& wget -q https://dl.bintray.com/jfrog/artifactory/jfrog-artifactory-
oss-${ARTIFACTORY_VERSION}.zip -O /opt/files/artifactory.zip \  
&& echo "$ARTIFACTORY_SHA256" /opt/files/artifactory.zip | sha256sum -c - \  
&& mkdir /opt/artifactory \  
&& unzip -q /opt/files/artifactory.zip -d /opt/artifactory/ \  
&& ln -s /opt/artifactory/artifactory-oss-${ARTIFACTORY_VERSION}
/opt/artifactory/current \  
&& rm /opt/files/artifactory.zip \  
&& wget -q https://jdbc.postgresql.org/download/${POSTGRES_JDBC_DRIVER} -O
/opt/files/${POSTGRES_JDBC_DRIVER} \  
&& echo "$POSTGRES_SHA256" /opt/files/${POSTGRES_JDBC_DRIVER} | sha256sum -c -  
  
COPY files /opt/files  
  
VOLUME /opt/artifactory/current/data  
VOLUME /opt/artifactory/current/logs  
VOLUME /opt/artifactory/current/backup  
  
WORKDIR ${ARTIFACTORY_HOME}  
  
EXPOSE 8081  
CMD ["/opt/files/startup.sh"]  
  

