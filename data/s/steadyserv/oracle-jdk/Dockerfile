FROM alpine:3.6  
  
ENV GLIBC_VERSION 2.25-r0  
RUN set -x \  
&& apk \--no-cache add --virtual .glibc-deps ca-certificates openssl \  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub \  
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk \  
&& apk add glibc-${GLIBC_VERSION}.apk \  
&& rm glibc-${GLIBC_VERSION}.apk \  
&& apk del .glibc-deps  
  
ENV JAVA_VERSION=7  
ENV JAVA_UPDATE=80  
ENV
JAVA_SHA256=bad9a731639655118740bee119139c1ed019737ec802a630dd7ad7aab4309623  
ENV MAVEN_MAJOR=3  
ENV MAVEN_VERSION=3.3.9  
  
ENV JAVA_HOME=/opt/jdk \  
MAVEN_HOME=/usr/local/maven \  
PATH=${PATH}:/opt/jdk/bin:/usr/local/maven/bin  
  
RUN set -x \  
&& apk add --no-cache --virtual .install-deps \  
ca-certificates \  
gnupg \  
openssl \  
tar \  
wget \  
&& JAVA_ARCHIVE="jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" \  
&& wget \--no-verbose "https://steadyserv-packages.s3.amazonaws.com/oracle-
jdk/${JAVA_ARCHIVE}" \  
&& echo "${JAVA_SHA256} *${JAVA_ARCHIVE}" > java_sha256 \  
&& sha256sum -c java_sha256 \  
&& mkdir /opt \  
&& tar xzf $JAVA_ARCHIVE -C /opt \  
&& ln -s /opt/jdk* $JAVA_HOME \  
&& chown -R root:root $JAVA_HOME/* \  
&& rm -f $JAVA_ARCHIVE java_sha256 $JAVA_HOME/src.zip \  
\  
&& maven_archive=apache-maven-${MAVEN_VERSION}-bin.tar.gz \  
&& wget \--no-verbose
http://apache.mirrors.tds.net/maven/maven-${MAVEN_MAJOR}/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& wget --no-verbose
https://archive.apache.org/dist/maven/maven-${MAVEN_MAJOR}/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz.asc \  
&& wget --no-verbose https://archive.apache.org/dist/maven/KEYS \  
&& gpg --import KEYS \  
&& gpg --batch --verify ${maven_archive}.asc ${maven_archive} \  
&& mkdir /usr/local/maven \  
&& tar -xzf ${maven_archive} -C /usr/local/maven --strip-components=1 \  
&& rm -rf ${maven_archive} ${maven_archive}.asc KEYS /root/.gnupg \  
\  
&& apk del .install-deps  

