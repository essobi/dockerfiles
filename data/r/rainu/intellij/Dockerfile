FROM openjdk:8-jdk-alpine  
MAINTAINER rainu <rainu@raysha.de>  
  
ENV INTELLIJ_LINK http://download.jetbrains.com/idea/ideaIU-2017.1.2.tar.gz  
ENV GOLANG http://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz  
  
ENV USERNAME intellij  
ENV GROUPNAME intellij  
  
#make home directory for intellij user  
RUN mkdir -p /home/intellij && \  
mkdir -p /home/intellij/bin &&\  
mkdir -p /home/intellij/.m2  
  
#install some additional packages  
#Here we install GNU libc (aka glibc) and set C.UTF-8 locale as default. (see
https://hub.docker.com/r/frolvlad/alpine-glibc/~/dockerfile/)  
RUN apk add --no-cache fontconfig git openssh && \  
ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
wget "https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" -O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget
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
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
apk del glibc-i18n && \  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
ENV LANG=C.UTF-8  
#download and extract intelliJ-Ultimate  
RUN wget $INTELLIJ_LINK -O /tmp/intellij.tar.gz &&\  
mkdir /opt/ &&\  
tar -xzvf /tmp/intellij.tar.gz -C /opt/ && mv /opt/$(ls /opt/) /opt/intellij/
&&\  
rm /tmp/intellij.tar.gz &&\  
rm -rf /opt/intellij/jre64 && ln -s $JAVA_HOME/jre /opt/intellij/jre64  
  
#download and extract golang  
RUN wget $GOLANG -O /tmp/golang.tar.gz &&\  
tar -xzvf /tmp/golang.tar.gz -C /usr/local/ &&\  
rm /tmp/golang.tar.gz  
  
COPY ./start.sh /home/intellij/start.sh  
  
ENTRYPOINT ["/home/intellij/start.sh"]  

