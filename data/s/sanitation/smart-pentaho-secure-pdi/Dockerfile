FROM sanitation/java-alpine:latest  
RUN apk add --no-cache --update-cache git  
  
MAINTAINER DSNY smart_inf@dsny.nyc.gov  
  
# Init ENV  
ENV PENTAHO_VERSION 8.0  
ENV PENTAHO_TAG 8.0.0.0-28  
  
ENV PENTAHO_HOME /opt/pentaho  
  
# Apply JAVA_HOME  
ENV PENTAHO_JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
  
RUN mkdir -p ${PENTAHO_HOME}; addgroup -g 999 pentaho && adduser -D -G pentaho
-s /bin/bash -h ${PENTAHO_HOME} pentaho; chown pentaho:pentaho ${PENTAHO_HOME}  
  
  
USER pentaho  
  
# Download Pentaho BI Server  
RUN /usr/bin/wget -c
https://sourceforge.net/projects/pentaho/files/Pentaho%208.0/client-tools/pdi-
ce-8.0.0.0-28.zip/download -O /tmp/pdi-ce-${PENTAHO_TAG}.zip; \  
/usr/bin/unzip -q /tmp/pdi-ce-${PENTAHO_TAG}.zip -d $PENTAHO_HOME; \  
rm /tmp/pdi-ce-${PENTAHO_TAG}.zip  
  
# This is to copy from local  
#COPY pdi-ce-8.0.0.0-28/ /opt/pentaho/  
  
COPY scripts/ /opt/pentaho/data-integration/  
COPY slave_dyn.xml /opt/pentaho/data-integration/  
COPY libs/sqljdbc42.jar /opt/pentaho/data-integration/lib/  
COPY libs/jtds-1.3.1.jar /opt/pentaho/data-integration/lib/  
COPY libs/mysql-connector-java-5.1.41-bin.jar /opt/pentaho/data-
integration/lib/  
COPY libs/ojdbc6.jar /opt/pentaho/data-integration/lib/  
#COPY ps_certs/ /opt/pentaho/data-integration/ps_certs/  
#RUN keytool -import -alias msdlva-dsnysmt11 -file /opt/pentaho/data-
integration/ps_certs/msdlva-dsnysmt11.csc.nycnet.cer -keystore
"$JAVA_HOME/jre/lib/security/cacerts" -storepass "changeit" -noprompt  
  
  
WORKDIR /opt/pentaho/data-integration  
  
EXPOSE 8181  
  
CMD ["./run.sh"]  

