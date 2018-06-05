# vim:set ft=dockerfile:  
FROM debian:jessie  
  
ENV BITBUCKET_HOME=/var/lib/bitbucket \  
BITBUCKET_INSTALL=/opt/atlassian/bitbucket \  
BITBUCKET_UID=7990 \  
BITBUCKET_USER=bitbucket \  
BITBUCKET_GID=7999 \  
BITBUCKET_GROUP=bitbucket \  
BITBUCKET_VERSION=4.14.5 \  
#  
GOSU_VERSION=1.7 \  
#  
JAVA_HOME=/usr/lib/jvm/java-8-oracle \  
JAVA_VERSION=8  
  
RUN set -x \  
&& export DEBIAN_FRONTEND=noninteractive \  
### Install ca-certificates so that wget won't complain about the cert for the
Oracle downloads site  
&& apt-get update \  
&& apt-get --assume-yes --no-install-recommends install \  
ca-certificates \  
### Add the Oracle JDK repo and pre-acknowledge the licenses  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
7B2C3B0889BF5709A105D03AC2518248EEA14886 \  
&& echo deb http://ppa.launchpad.net/webupd8team/java/ubuntu vivid main >
/etc/apt/sources.list.d/webupd8team-java-ubuntu-vivid.list \  
&& echo oracle-java${JAVA_VERSION}-installer shared/accepted-oracle-
license-v1-1 select true | debconf-set-selections \  
&& echo oracle-java${JAVA_VERSION}-unlimited-jce-policy shared/accepted-
oracle-license-v1-1 select true | debconf-set-selections \  
### Get an updated list of packages that can be installed/upgraded which will
now include the Oracle JDKs  
&& apt-get update \  
### Install Oracle JDK, making it the default JVM  
&& apt-get --assume-yes --no-install-recommends install \  
oracle-java${JAVA_VERSION}-installer=${JAVA_VERSION}* \  
oracle-java${JAVA_VERSION}-unlimited-jce-policy=${JAVA_VERSION}* \  
oracle-java${JAVA_VERSION}-set-default=${JAVA_VERSION}* \  
### Install the Tomcat Native and APR shared objects  
libapr1 \  
libaprutil1 \  
libtcnative-1 \  
### Install curl, git, ssh, and wget along with ca-certificates-java  
ca-certificates-java \  
curl \  
git \  
openssh-client \  
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
### Install gosu  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture)" \  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/${GOSU_VERSION}/gosu-$(dpkg
--print-architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
### Install Bitbucket  
&& mkdir -p ${BITBUCKET_INSTALL} ${BITBUCKET_HOME}
/etc/java-${JAVA_VERSION}-oracle \  
&& groupadd -g ${BITBUCKET_GID} ${BITBUCKET_GROUP} \  
&& useradd -d ${BITBUCKET_INSTALL} -u ${BITBUCKET_UID} -g ${BITBUCKET_GID} -c
"Atlassian Bitbucket" ${BITBUCKET_USER} \  
&& wget --progress=dot:mega -O-
"https://www.atlassian.com/software/stash/downloads/binary/atlassian-
bitbucket-${BITBUCKET_VERSION}.tar.gz" | tar -xz --strip=1 -C
"${BITBUCKET_INSTALL}" \  
&& echo "BITBUCKET_USER=\"${BITBUCKET_USER}\";export BITBUCKET_USER" >
${BITBUCKET_INSTALL}/bin/user.sh \  
&& echo "bitbucket.home=${BITBUCKET_HOME}" > ${BITBUCKET_INSTALL}/atlassian-
bitbucket/WEB-INF/classes/bitbucket-application.properties \  
&& chmod -R 700 ${BITBUCKET_INSTALL} ${BITBUCKET_HOME} \  
&& chown -R ${BITBUCKET_USER}:${BITBUCKET_GROUP} \  
${BITBUCKET_HOME} \  
${BITBUCKET_INSTALL} \  
/etc/default/cacerts \  
/etc/java-${JAVA_VERSION}-oracle \  
/etc/ssl \  
&& find ${BITBUCKET_INSTALL} -name "*.sh" | xargs chmod -v +x \  
### Let the JVM find the Tomcat Native and APR shared objects  
&& ln -sv /usr/lib/x86_64-linux-gnu/libtcnative-1.so
${BITBUCKET_INSTALL}/lib/native/ \  
### Cleanup  
&& apt-get clean \  
&& rm -rf \  
/etc/java-6-sun \  
/tmp/* \  
/var/cache/oracle-* \  
/var/lib/apt/lists/* \  
/var/tmp/*  
  
COPY src/main/container/srv/ /srv/  
### Not a fan of the extra layer but I am very much a fan of docker build
caching many megabytes of lower layers  
RUN set -x \  
&& find /srv/ -name "*.sh" | xargs chmod -v +x  
# HTTP SSH  
EXPOSE 7990 7999  
  
WORKDIR ${BITBUCKET_INSTALL}  
  
VOLUME ["${BITBUCKET_HOME}"]  
  
ENTRYPOINT ["/srv/bitbucket.sh"]  
CMD ["bitbucket"]  

