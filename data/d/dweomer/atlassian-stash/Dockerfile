# vim:set ft=dockerfile:  
FROM ubuntu:vivid  
  
ENV STASH_HOME=/var/lib/stash \  
STASH_INSTALL=/opt/atlassian/stash \  
STASH_UID=7990 \  
STASH_USER=stash \  
STASH_GID=7999 \  
STASH_GROUP=stash \  
STASH_VERSION=3.11.2 \  
#  
JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
JAVA_VERSION=8 \  
JAVA_UPDATE=60  
  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
### Install ca-certificates so that wget won't complain about the cert for the
Oracle downloads site  
&& apt-get --assume-yes \--no-install-recommends install \  
ca-certificates \  
### Add the Oracle JDK repo and pre-acknowledge the licenses  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
7B2C3B0889BF5709A105D03AC2518248EEA14886 \  
&& echo deb http://ppa.launchpad.net/webupd8team/java/ubuntu vivid main >
/etc/apt/sources.list.d/webupd8team-ubuntu-java-vivid.list \  
&& echo oracle-java${JAVA_VERSION}-installer shared/accepted-oracle-
license-v1-1 select true | debconf-set-selections \  
&& echo oracle-java${JAVA_VERSION}-unlimited-jce-policy shared/accepted-
oracle-license-v1-1 select true | debconf-set-selections \  
### Get an updated list of packages that can be installed/upgraded which will
now include the Oracle JDKs  
&& apt-get update \  
### Install Oracle JDK, making it the default JVM  
&& apt-get --assume-yes \--no-install-recommends install \  
oracle-java${JAVA_VERSION}-installer=${JAVA_VERSION}u${JAVA_UPDATE}* \  
oracle-java${JAVA_VERSION}-unlimited-jce-
policy=${JAVA_VERSION}u${JAVA_UPDATE}* \  
oracle-java${JAVA_VERSION}-set-default=${JAVA_VERSION}u${JAVA_UPDATE}* \  
### Install the Tomcat Native and APR shared objects  
libapr1 \  
libaprutil1 \  
libtcnative-1 \  
### Install curl, git, ssh, and wget along with ca-certificates-java  
ca-certificates-java \  
curl \  
git \  
openssh-client \  
perl \  
wget \  
xmlstarlet \  
### Patch the ca-certificates-java script to use our Java  
&& sed -i -e 's/java-6-sun/java-${JAVA_VERSION}-oracle/g' /etc/ca-
certificates/update.d/jks-keystore \  
&& update-ca-certificates \  
### Modify the JDK installation to use our local cacerts  
&& mv -v ${JAVA_HOME}/jre/lib/security/cacerts
${JAVA_HOME}/jre/lib/security/cacerts.original \  
&& ln -vs /etc/ssl/certs/java/cacerts ${JAVA_HOME}/jre/lib/security/ \  
### Let the JVM find the Tomcat Native and APR shared objects  
&& ln -sv /usr/lib/x86_64-linux-gnu /usr/lib64 \  
### Install Stash  
&& mkdir -p ${STASH_INSTALL} ${STASH_HOME} /etc/java-${JAVA_VERSION}-oracle \  
&& groupadd -g ${STASH_GID} ${STASH_GROUP} \  
&& useradd -d ${STASH_INSTALL} -u ${STASH_UID} -g ${STASH_GID} -c "Atlassian
Stash" ${STASH_USER} \  
&& wget --progress=dot:mega -O-
"https://www.atlassian.com/software/stash/downloads/binary/atlassian-
stash-${STASH_VERSION}.tar.gz" | tar -xz --strip=1 -C "${STASH_INSTALL}" \  
&& echo "STASH_USER=\"${STASH_USER}\";export STASH_USER" >
${STASH_INSTALL}/bin/user.sh \  
&& echo "stash.home=${STASH_HOME}" > ${STASH_INSTALL}/atlassian-stash/WEB-
INF/classes/stash-application.properties \  
&& chmod -R 700 ${STASH_INSTALL} ${STASH_HOME} \  
&& chown -R ${STASH_USER}:${STASH_GROUP} \  
${STASH_HOME} \  
${STASH_INSTALL} \  
/etc/default/cacerts \  
/etc/java-${JAVA_VERSION}-oracle \  
/etc/ssl \  
&& find ${STASH_INSTALL} -name "*.sh" | xargs chmod -v +x \  
### Cleanup  
&& apt-get clean \  
&& rm -rf /etc/java-6-sun /tmp/* /var/tmp/* /var/cache/oracle-*
/var/lib/apt/lists/*  
  
COPY src/main/container/srv/ /srv/  
### Not a fan of the extra layer but I am very much a fan of docker build
caching many megabytes of lower layers  
RUN set -x \  
&& find /srv/ -name "*.sh" | xargs chmod -v +x  
  
USER ${STASH_USER}:${STASH_GROUP}  
  
VOLUME ["${STASH_HOME}"]  
  
# HTTP SSH  
EXPOSE 7990 7999  
  
WORKDIR ${STASH_INSTALL}  
  
ENTRYPOINT ["/srv/stash.sh"]  
CMD ["stash"]  

