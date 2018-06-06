#  
# BUILD : DF/[ATLASSIAN][CONFLUENCE]  
# OS/CORE : dunkelfrosch/alpine-jdk8  
# SERVICES : ntp, ...  
#  
# VERSION 1.0.5  
#  
FROM dunkelfrosch/alpine-jdk8  
  
LABEL maintainer="Patrick Paechnatz <patrick.paechnatz@gmail.com>" \  
com.container.vendor="dunkelfrosch impersonate" \  
com.container.service="atlassian/confluence" \  
com.container.priority="1" \  
com.container.project="confluence" \  
img.version="1.0.5" \  
img.description="atlassian confluence application container"  
  
ARG ISO_LANGUAGE=en  
ARG ISO_COUNTRY=US  
ARG CONFLUENCE_VERSION=6.8.1  
ARG MYSQL_CONNECTOR_VERSION=5.1.46  
ENV TERM="xterm" \  
TIMEZONE="Europe/Berlin" \  
CONFLUENCE_HOME="/var/atlassian/application-data/confluence" \  
CONFLUENCE_INSTALL_DIR="/opt/atlassian/confluence" \  
CONFLUENCE_DOWNLOAD_URL="http://www.atlassian.com/software/confluence/downloads/binary"
\  
JVM_MYSQL_CONNECTOR_URL="http://dev.mysql.com/get/Downloads/Connector-J" \  
RUN_USER="confluence" \  
RUN_GROUP="confluence" \  
RUN_UID=1000 \  
RUN_GID=1000  
COPY scripts/*.sh /usr/bin/  
  
RUN set -e && \  
apk add --update ca-certificates gzip curl tar xmlstarlet msttcorefonts-
installer ttf-dejavu fontconfig ghostscript graphviz motif wget tzdata bash &&
\  
update-ms-fonts && fc-cache -f && \  
/usr/glibc-compat/bin/localedef -i ${ISO_LANGUAGE}_${ISO_COUNTRY} -f UTF-8
${ISO_LANGUAGE}_${ISO_COUNTRY}.UTF-8 && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" >/etc/timezone && \  
ln -s /usr/bin/dockerwait.sh /usr/bin/dockerwait  
  
# --  
# download/prepare newest mysql connector  
# --  
RUN set -e && \  
export CONTAINER_USER=$RUN_USER && \  
export CONTAINER_GROUP=$RUN_GROUP && \  
addgroup -g ${RUN_GID} ${RUN_GROUP} && \  
adduser -u ${RUN_UID} \  
-G ${RUN_GROUP} \  
-h /home/${RUN_USER} \  
-s /bin/sh \  
-S ${RUN_USER}  
  
# --  
# download/prepare confluence  
# --  
RUN set -e && \  
mkdir -p ${CONFLUENCE_HOME} \  
${CONFLUENCE_INSTALL_DIR}/conf \  
${CONFLUENCE_INSTALL_DIR}/lib \  
${CONFLUENCE_INSTALL_DIR}/confluence/WEB-INF/lib \  
/home/confluence && \  
curl -L --progress-bar "${CONFLUENCE_DOWNLOAD_URL}/atlassian-
confluence-${CONFLUENCE_VERSION}.tar.gz" | tar -xz --strip-components=1 -C
"${CONFLUENCE_INSTALL_DIR}"  
  
# --  
# copy main entrypoint script to root path  
# --  
RUN set -e && \  
export KEYSTORE=$JAVA_HOME/jre/lib/security/cacerts && \  
wget -q -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx1.der && \  
wget -q -P /tmp/ https://letsencrypt.org/certs/letsencryptauthorityx2.der && \  
wget -q -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x1-cross-
signed.der && \  
wget -q -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x2-cross-
signed.der && \  
wget -q -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x3-cross-
signed.der && \  
wget -q -P /tmp/ https://letsencrypt.org/certs/lets-encrypt-x4-cross-
signed.der && \  
keytool -trustcacerts -keystore ${KEYSTORE} -storepass changeit -noprompt
-importcert -alias isrgrootx1 -file /tmp/letsencryptauthorityx1.der && \  
keytool -trustcacerts -keystore ${KEYSTORE} -storepass changeit -noprompt
-importcert -alias isrgrootx2 -file /tmp/letsencryptauthorityx2.der && \  
keytool -trustcacerts -keystore ${KEYSTORE} -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx1 -file /tmp/lets-encrypt-x1-cross-
signed.der && \  
keytool -trustcacerts -keystore ${KEYSTORE} -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx2 -file /tmp/lets-encrypt-x2-cross-
signed.der && \  
keytool -trustcacerts -keystore ${KEYSTORE} -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx3 -file /tmp/lets-encrypt-x3-cross-
signed.der && \  
keytool -trustcacerts -keystore ${KEYSTORE} -storepass changeit -noprompt
-importcert -alias letsencryptauthorityx4 -file /tmp/lets-encrypt-x4-cross-
signed.der && \  
wget -O /SSLPoke.class
https://confluence.atlassian.com/kb/files/779355358/779355357/1/1441897666313/SSLPoke.class  
  
RUN set -e && \  
rm -f ${CONFLUENCE_INSTALL_DIR}/lib/mysql-connector-java*.jar && \  
curl -Ls "${JVM_MYSQL_CONNECTOR_URL}/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}.tar.gz" | tar -xz --strip-components=1 -C
"/tmp" && \  
mv /tmp/mysql-connector-java-${MYSQL_CONNECTOR_VERSION}-bin.jar
${CONFLUENCE_INSTALL_DIR}/confluence/WEB-INF/lib && \  
cp -f ${CONFLUENCE_INSTALL_DIR}/confluence/WEB-INF/lib/mysql-connector-
java-${MYSQL_CONNECTOR_VERSION}-bin.jar ${CONFLUENCE_INSTALL_DIR}/lib/mysql-
connector-java-${MYSQL_CONNECTOR_VERSION}-bin.jar && \  
sed -i -e 's/-Xms\\([0-9]\\+[kmg]\\)
-Xmx\\([0-9]\\+[kmg]\\)/-Xms\${JVM_MINIMUM_MEMORY:=\1}
-Xmx\${JVM_MAXIMUM_MEMORY:=\2} \${JVM_SUPPORT_RECOMMENDED_ARGS}
-Dconfluence.home=\${CONFLUENCE_HOME}/g'
${CONFLUENCE_INSTALL_DIR}/bin/setenv.sh && \  
chown -R ${RUN_USER}:${RUN_GROUP} ${CONFLUENCE_HOME} ${CONFLUENCE_INSTALL_DIR}
&& \  
chmod -R 700 ${CONFLUENCE_HOME} ${CONFLUENCE_INSTALL_DIR} && \  
apk del ca-certificates wget curl unzip tzdata msttcorefonts-installer  
  
# --  
# define container execution behaviour  
# --  
EXPOSE 8090 8091  
USER confluence  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME ["${CONFLUENCE_HOME}"]  
  
WORKDIR ${CONFLUENCE_HOME}  
  
ENTRYPOINT ["/sbin/tini","--","/entrypoint.sh"]  
  
CMD ["confluence"]  

