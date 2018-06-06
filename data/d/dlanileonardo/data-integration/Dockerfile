FROM java:7  
MAINTAINER Dlani Mendes dlanileonardo@gmail.com  
  
LABEL org.label-schema.vcs-url="https://github.com/dlanileonardo/docker-data-
integration" \  
org.label-schema.vendor=dlanileonardo \  
org.label-schema.name=data-integration \  
io.wikiwi.license=MIT  
  
# Init ENV  
ENV DATA_INTEGRATION_VERSION 5.3  
ENV DATA_INTEGRATION_TAG 5.3.0.0-213  
ENV PENTAHO_HOME /opt/pentaho  
  
# Apply JAVA_HOME  
RUN . /etc/environment  
ENV PENTAHO_JAVA_HOME $JAVA_HOME  
ENV PENTAHO_JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-amd64  
ENV KETTLE_HOME /var  
  
RUN apt-get update; apt-get -y upgrade  
  
RUN /usr/bin/wget --progress=dot:giga
http://downloads.sourceforge.net/project/pentaho/Data%20Integration/${DATA_INTEGRATION_VERSION}/pdi-
ce-${DATA_INTEGRATION_TAG}.zip -O /tmp/pdi-ce-${DATA_INTEGRATION_TAG}.zip; \  
/usr/bin/unzip -q /tmp/pdi-ce-${DATA_INTEGRATION_TAG}.zip -d $PENTAHO_HOME; \  
chmod +x $PENTAHO_HOME/data-integration/*.sh; \  
rm -rf /tmp/pdi-ce-${DATA_INTEGRATION_TAG}.zip  
  
COPY kettle /var/.kettle  
COPY scripts $PENTAHO_HOME/scripts  
COPY configuration.xml $PENTAHO_HOME/data-integration  
  
WORKDIR /var/etl  
EXPOSE 8080  
CMD ["sh", "$PENTAHO_HOME/scripts/run.sh"]  
  
# RUN mkdir ${PENTAHO_HOME}; useradd -s /bin/bash -d ${PENTAHO_HOME} pentaho;
chown pentaho:pentaho ${PENTAHO_HOME}  
# USER pentaho

