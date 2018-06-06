FROM alpine:3.4  
MAINTAINER dadez <dadez@protonmail.com>  
  
ADD ./SwissGovernmentRootCAII.pem /tmp/  
  
# build parameters  
ARG JAVA_DISTRIBUTION=server-jre  
#ARG JAVA_DISTRIBUTION=jdk  
ARG JAVA_MAJOR_VERSION=${JAVA_MAJOR_VERSION:-8}  
ARG JAVA_UPDATE_VERSION=${JAVA_UPDATE_VERSION:-111}  
ARG JAVA_BUILD_NUMBER=${JAVA_BUILD_NUMBER:-14}  
ARG GLIBC_VERSION=2.23-r1  
  
ARG CERT=SwissGovernmentRootCAII.pem  
ARG ALIAS=SwissGovernmentRootCAII  
ARG STORE=jre/lib/security/cacerts  
ARG STOREPASS="dsjflkjsdklfjsdklfjsdklfjkldsjf"  
  
ENV TIMEZONE Europe/Zurich  
ENV LANG en_US.UTF-8  
ENV JAVA_VERSION=1.${JAVA_MAJOR_VERSION}.0_${JAVA_UPDATE_VERSION}  
ENV JAVA_HOME=/opt/java/${JAVA_DISTRIBUTION}${JAVA_VERSION}  
ENV PATH=$PATH:$JAVA_HOME/bin  
  
#override proxy settings  
ENV http_proxy=""  
ENV https_proxy=""  
  
RUN export
JAVA_TARBALL=${JAVA_DISTRIBUTION}-${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-linux-x64.tar.gz
\  
# Install tooling  
&& apk add --update \  
ca-certificates \  
unzip \  
wget \  
tzdata \  
  
#set timezone  
&& echo $TIMEZONE > /etc/timezone \  
&& cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \  
  
# Install latest glibc  
&& wget \--directory-prefix=/tmp https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \  
apk add --allow-untrusted /tmp/glibc-${GLIBC_VERSION}.apk \  
&& wget --directory-prefix=/tmp https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk && \  
apk add --allow-untrusted /tmp/glibc-bin-${GLIBC_VERSION}.apk \  
&& wget \--directory-prefix=/tmp https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-i18n-${GLIBC_VERSION}.apk && \  
apk --allow-untrusted add /tmp/glibc-i18n-${GLIBC_VERSION}.apk \  
&& /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 \  
  
# Install oracle java  
&& wget --directory-prefix=/tmp \  
\--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_MAJOR_VERSION}u${JAVA_UPDATE_VERSION}-b${JAVA_BUILD_NUMBER}/${JAVA_TARBALL}
\  
&& mkdir -p /opt/java \  
&& tar -xzf /tmp/${JAVA_TARBALL} -C /opt/java/ \  
&& if [ "${JAVA_DISTRIBUTION}" = "server-jre" ]; \  
then mv /opt/java/jdk${JAVA_VERSION} ${JAVA_HOME} ; \  
fi \  
&& ln -s ${JAVA_HOME}/bin/java /usr/bin/java \  
  
#install jce policy  
&& wget --directory-prefix=/tmp \  
\--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jce/${JAVA_MAJOR_VERSION}/jce_policy-${JAVA_MAJOR_VERSION}.zip \  
&& unzip -jo /tmp/jce_policy-${JAVA_MAJOR_VERSION}.zip *.jar -d
${JAVA_HOME}/jre/lib/security/ \  
  
# Remove obsolete packages  
&& apk del \  
ca-certificates \  
unzip \  
wget \  
tzdata \  
  
# empty keystore  
&& rm -f ${JAVA_HOME}/${STORE} \  
&& $JAVA_HOME/bin/keytool -import -file /tmp/${CERT} -alias ${ALIAS} -keystore
${JAVA_HOME}/${STORE} -storepass $STOREPASS -noprompt \  
  
# Clean caches and tmps  
&& rm -rf /var/cache/apk/* \  
/tmp/* \  
/var/log/*  

