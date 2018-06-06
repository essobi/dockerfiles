FROM openjdk:8-alpine  
  
# Configuration variables.  
ENV FISHEYE_VERSION=4.5.1 \  
FISHEYE_HOME=/var/atlassian/application-data/fisheye \  
FISHEYE_INSTALL=/opt/atlassian/fisheye \  
MYSQL_VERSION=5.1.38  
RUN set -x \  
&& apk add --no-cache libressl wget tar bash unzip git \  
&& mkdir -p "${FISHEYE_HOME}" \  
&& mkdir -p "${FISHEYE_INSTALL}" \  
&& wget -O "atlassian-fisheye-${FISHEYE_VERSION}.zip" \--no-verbose
"https://www.atlassian.com/software/fisheye/downloads/binary/fisheye-${FISHEYE_VERSION}.zip"
\  
&& wget -O "mysql-connector-java-${MYSQL_VERSION}.tar.gz" \--no-verbose
"https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-${MYSQL_VERSION}.tar.gz" \  
&& unzip -o atlassian-fisheye-${FISHEYE_VERSION}.zip -d /tmp \  
&& yes | cp -rf /tmp/fecru-${FISHEYE_VERSION}/* ${FISHEYE_INSTALL}/. \  
&& tar -xzvf "mysql-connector-java-${MYSQL_VERSION}.tar.gz" -C
"${FISHEYE_INSTALL}/lib" \--strip-components=1 \  
&& rm -rf /tmp/fecru-${FISHEYE_VERSION}/*.* \  
&& rm -rf "mysql-connector-java-${MYSQL_VERSION}.tar.gz" \  
&& rm -rf "atlassian-fisheye-${FISHEYE_VERSION}.zip" \  
&& adduser -D -u 1000 fisheye \  
&& chown -R fisheye "${FISHEYE_HOME}" \  
&& chown -R fisheye "${FISHEYE_INSTALL}" \  
&& chmod -R 700 "${FISHEYE_HOME}" \  
&& chmod -R 700 "${FISHEYE_INSTALL}"  
  
# Expose default HTTP connector port.  
EXPOSE 8060  
VOLUME [ "${FISHEYE_HOME}" ]  
  
WORKDIR ${FISHEYE_INSTALL}  
  
USER fisheye  
  
ENTRYPOINT ["bin/fisheyectl.sh", "run"]  

