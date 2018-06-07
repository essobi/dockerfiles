FROM alpine:3.7  
MAINTAINER Sonatype <dev@sonatype.com>  
  
ENV JAVA_HOME=/opt/java \  
JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=172 \  
JAVA_VERSION_BUILD=11 \  
JAVA_DOWNLOAD_HASH=a58eab1ec242421181065cdc37240b08 \  
GLIBC_VERSION=2.27-r0 \  
DOCKERIZE_VERSION=v0.6.1  
# interpolated settings need to go in separate layer  
ENV JAVA_URL=http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_DOWNLOAD_HASH}/server-
jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \  
GLIBC_URL=https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION} \  
DOCKERIZE_URL=https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-
linux-amd64-${DOCKERIZE_VERSION}.tar.gz  
  
RUN apk upgrade --update \  
&& apk add --update bash curl ca-certificates \  
&& for pkg in glibc glibc-bin glibc-i18n; do \  
curl -sSL ${GLIBC_URL}/${pkg}-${GLIBC_VERSION}.apk -o /tmp/${pkg}.apk; \  
done \  
&& apk add --allow-untrusted /tmp/*.apk \  
&& rm -v /tmp/*.apk \  
&& /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 \  
&& /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib \  
&& curl -sSL ${DOCKERIZE_URL} | tar -C /usr/local/bin -xz  
  
# install Oracle JRE  
RUN mkdir -p /opt \  
&& curl --fail --silent --location --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie; " ${JAVA_URL} \  
| tar -xz -C /opt \  
&& ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JAVA_HOME}  

