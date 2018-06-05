FROM debian:jessie  
MAINTAINER Krzysztof Kardasz <krzysztof@kardasz.eu>  
  
# Update system and install required packages  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install git, download and extract Stash and create the required directory
layout.  
# Try to limit the number of RUN instructions to minimise the number of layers
that will need to be created.  
RUN apt-get update -qq \  
&& apt-get install -y wget curl git unzip \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
# Download Oracle JDK  
ENV ORACLE_JDK_VERSION jdk-8u92  
ENV ORACLE_JDK_URL http://download.oracle.com/otn-
pub/java/jdk/8u92-b14/jdk-8u92-linux-x64.tar.gz  
RUN mkdir -p /opt/jdk/$ORACLE_JDK_VERSION && \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie" -O
/opt/jdk/$ORACLE_JDK_VERSION/$ORACLE_JDK_VERSION.tar.gz $ORACLE_JDK_URL && \  
tar -zxf /opt/jdk/$ORACLE_JDK_VERSION/$ORACLE_JDK_VERSION.tar.gz --strip-
components=1 -C /opt/jdk/$ORACLE_JDK_VERSION && \  
rm /opt/jdk/$ORACLE_JDK_VERSION/$ORACLE_JDK_VERSION.tar.gz && \  
update-alternatives --install /usr/bin/java java
/opt/jdk/$ORACLE_JDK_VERSION/bin/java 100 && \  
update-alternatives --install /usr/bin/javac javac
/opt/jdk/$ORACLE_JDK_VERSION/bin/javac 100  
  
ENV DOWNLOAD_URL
https://downloads.atlassian.com/software/stash/downloads/atlassian-bitbucket-  
  
# https://confluence.atlassian.com/display/STASH/Stash+home+directory  
ENV BITBUCKET_HOME /var/atlassian/application-data/bitbucket  
  
  
ENV JAVA_HOME /opt/jdk/${ORACLE_JDK_VERSION}  
ENV JAVA_TRUSTSTORE ${JAVA_HOME}/jre/lib/security/cacerts  
ENV JAVA_TRUSTSTORE_PASSWORD changeit  
  
# Use the default unprivileged account. This could be considered bad practice  
# on systems where multiple processes end up being executed by 'daemon' but  
# here we only ever run one process anyway.  
ENV RUN_USER atlassian  
ENV RUN_USER_UID 5000  
ENV RUN_GROUP atlassian  
ENV RUN_GROUP_GID 5000  
RUN \  
groupadd --gid ${RUN_GROUP_GID} -r ${RUN_GROUP} && \  
useradd -r --uid ${RUN_USER_UID} -g ${RUN_GROUP} ${RUN_USER}  
  
# Install Atlassian Stash to the following location  
ENV BITBUCKET_INSTALL_DIR /opt/atlassian/bitbucket  
  
ENV BITBUCKET_VERSION 4.0.1  
RUN mkdir -p ${BITBUCKET_INSTALL_DIR} \  
&& curl -L --silent ${DOWNLOAD_URL}${BITBUCKET_VERSION}.tar.gz | tar -xz
--strip=1 -C "$BITBUCKET_INSTALL_DIR" \  
&& mkdir -p ${BITBUCKET_INSTALL_DIR}/conf/Catalina \  
&& chown -R root:root ${BITBUCKET_INSTALL_DIR}/ \  
&& chmod -R 755 ${BITBUCKET_INSTALL_DIR}/ \  
&& chmod -R 700 ${BITBUCKET_INSTALL_DIR}/conf/Catalina \  
&& chmod -R 700 ${BITBUCKET_INSTALL_DIR}/logs \  
&& chmod -R 700 ${BITBUCKET_INSTALL_DIR}/temp \  
&& chmod -R 700 ${BITBUCKET_INSTALL_DIR}/work \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_INSTALL_DIR}/logs \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_INSTALL_DIR}/temp \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_INSTALL_DIR}/work \  
&& chown -R ${RUN_USER}:${RUN_GROUP} ${BITBUCKET_INSTALL_DIR}/conf  
  
# MySQL connector, mail api, activation api  
RUN \  
wget --header "Cookie: oraclelicense=accept-securebackup-cookie" -O
${BITBUCKET_INSTALL_DIR}/jaf-1_1_1.zip http://download.oracle.com/otn-
pub/java/jaf/1.1.1/jaf-1_1_1.zip && \  
unzip ${BITBUCKET_INSTALL_DIR}/jaf-1_1_1.zip -d ${BITBUCKET_INSTALL_DIR} && \  
mv ${BITBUCKET_INSTALL_DIR}/jaf-1.1.1/activation.jar
${BITBUCKET_INSTALL_DIR}/lib/ && \  
rm -rf ${BITBUCKET_INSTALL_DIR}/jaf-1.1.1
${BITBUCKET_INSTALL_DIR}/jaf-1_1_1.zip && \  
wget -O ${BITBUCKET_INSTALL_DIR}/mail-1.5.4.jar
http://java.net/projects/javamail/downloads/download/javax.mail.jar && \  
mv ${BITBUCKET_INSTALL_DIR}/mail-1.5.4.jar ${BITBUCKET_INSTALL_DIR}/lib/ && \  
wget -O ${BITBUCKET_INSTALL_DIR}/mysql-connector-java-5.1.38.tar.gz
http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.38.tar.gz && \  
tar xzf ${BITBUCKET_INSTALL_DIR}/mysql-connector-java-5.1.38.tar.gz -C
${BITBUCKET_INSTALL_DIR} && \  
mv ${BITBUCKET_INSTALL_DIR}/mysql-connector-java-5.1.38/mysql-connector-
java-5.1.38-bin.jar ${BITBUCKET_INSTALL_DIR}/lib/ && \  
rm -rf ${BITBUCKET_INSTALL_DIR}/mysql-connector-java-5.1.38.tar.gz
${BITBUCKET_INSTALL_DIR}/mysql-connector-java-5.1.38 && \  
rm -f ${BITBUCKET_INSTALL_DIR}/atlassian-bitbucket/WEB-
INF/lib/{activation,mail}-*.jar  
  
USER ${RUN_USER}:${RUN_GROUP}  
  
VOLUME ["${BITBUCKET_INSTALL_DIR}"]  
  
# HTTP Port  
EXPOSE 7990  
# SSH Port  
EXPOSE 7999  
WORKDIR $BITBUCKET_INSTALL_DIR  
  
# Run in foreground  
CMD ["./bin/start-bitbucket.sh", "-fg"]  

