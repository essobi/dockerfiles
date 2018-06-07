FROM ubuntu:16.04  
#Forked from maintainer Carlos Moro  
LABEL author="Nicolae Rosu" \  
maintainer="rnicolae90@gmailcom" \  
version="0.4.7" \  
description="Almost ready for production TOMCAT"  
  
ARG USER=tom  
ARG GROUP=cat  
ARG uid=27300  
ARG gid=27300  
ENV TOMCAT_VERSION=8.5.16 \  
CATALINA_HOME="/opt/tomcat" \  
TOMCAT_LOG="/var/log/catalina" \  
TOMCAT_WEBAPPS="${CATALINA_HOME}/webapps" \  
TOMCAT_MANAGER=${TOMCAT_MANAGER:-/opt/tomcat/webapps} \  
JAVA_HOME="/usr/lib/jvm/java-8-oracle" \  
MANAGER_ALLOW_REMOTE=${MANAGER_ALLOW_REMOTE:-false} \  
MANAGER_USER=${MANAGER_USER:-admin} \  
MANAGER_PASSWORD=${MANAGER_PASSWORD:-admin} \  
PATH=${PATH}:${CATALINA_HOME}/bin \  
DOCKER_IMAGE_VALUE=${DOCKER_IMAGE_VALUE:-prod}  
  
#VOLUME ${CATALINA_HOME}  
# Set the locale install PPA, install Tomcat.  
RUN groupadd -g ${gid} ${GROUP} \  
&& useradd -d "/home/tomcat/" -u ${uid} -g ${gid} -m -s /bin/bash ${USER}  
  
VOLUME ${TOMCAT_WEBAPPS}  
  
RUN echo 'deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main' >>
/etc/apt/sources.list && \  
echo 'deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main' >>
/etc/apt/sources.list && \  
apt-get clean && apt-get update && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get install -y --force-yes --no-install-recommends oracle-java8-installer
&& \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
wget --quiet --no-cookies
http://mirrors.m247.ro/apache/tomcat/tomcat-8/v${TOMCAT_VERSION}/bin/apache-
tomcat-${TOMCAT_VERSION}.tar.gz -O /tmp/tomcat.tgz && \  
mkdir -p ${CATALINA_HOME}/ && \  
tar xzvf /tmp/tomcat.tgz --strip 1 -C ${CATALINA_HOME}/ && \  
chown -R ${USER}:${GROUP} ${CATALINA_HOME} && \  
rm -rf /tmp/*  
  
# Add admin/admin user  
ADD tomcat-users.xml ${CATALINA_HOME}/conf/  
ADD entrypoint.sh /  
  
EXPOSE 8080 8009  
#VOLUME ["${TOMCAT_WEBAPPS}", "${TOMCAT_LOG}"]  
#ADD ["host-manager","manager","/opt/tomcat/webapps/"]  
#WORKDIR ${CATALINA_HOME}  
# Launch Tomcat  
RUN chown -R ${USER}: ${CATALINA_HOME} /entrypoint.sh  
USER ${USER}:${GROUP}  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["start"]  

