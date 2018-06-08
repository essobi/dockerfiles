FROM docker:18.01.0-ce-dind  
ENV COMPOSE_VERSION=1.19.0-rc3  
ENV JAVA_ALPINE_VERSION 8.151.12-r0  
ENV VAGRANT_VERSION=2.0.2  
#little overkill with pip but I'm LAZY! and as there will be ansible....  
RUN apk add --no-cache py-pip  
RUN pip install docker-compose=="$COMPOSE_VERSION"  
  
###################################################################################  
# OPENJDK TAKEN FROM  
# https://github.com/docker-
library/openjdk/blob/0476812eabd178c77534f3c03bd0a2673822d7b9/8-jdk/alpine/Dockerfile  
ENV LANG C.UTF-8  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
ENV JAVA_VERSION 8u111  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
#############################################################  
# Other  
RUN apk add --no-cache bash  
RUN apk add --no-cache git openssh  
RUN rm -R usr/lib/python2.7/site-packages/PyYAML-3.12-py2.7.egg-info  
RUN apk add --no-cache ansible  
  
##############################################################  
#VAGRANT, taken from https://hub.docker.com/r/kenney/vagrant-
alpine/~/dockerfile/  
# Install Vagrant  
RUN set -x && \  
apk add --no-cache bash rsync openssh ruby curl ruby-dev && \  
curl -L
https://releases.hashicorp.com/vagrant/${VAGRANT_VERSION}/vagrant_${VAGRANT_VERSION}_x86_64.deb
-O && \  
apk add --no-cache --virtual .vagrant dpkg tar && \  
dpkg -x vagrant_${VAGRANT_VERSION}_x86_64.deb / && \  
apk del .vagrant  
  
RUN rm -f vagrant_${VAGRANT_VERSION}_x86_64.deb  
  
# Install glibc  
#  
# originally source is:  
# https://github.com/frol/docker-alpine-
glibc/blob/5841d069eea61d12adaed2850e34b7c96199cac1/Dockerfile  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
wget \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
\  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
RUN vagrant plugin install docker  
  
RUN apk add --no-cache openssl  
#  
##############################################################  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
ENTRYPOINT ["/start.sh"]  
CMD [""]

