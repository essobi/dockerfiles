FROM alpine:latest  
  
MAINTAINER nisnaker <nisnaker@gmail.com>  
  
RUN APKTOOL_VERSION="2.1.1" && \  
APKTOOL_SCRIPT_URL="http://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool"
&& \  
APKTOOL_JAR_URL="https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_$APKTOOL_VERSION.jar"
&& \  
APKTOOL_SCRIPT_PATH="/usr/local/bin/apktool" && \  
apk --update add openjdk8-jre && \  
apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
wget $APKTOOL_SCRIPT_URL -O $APKTOOL_SCRIPT_PATH && \  
wget $APKTOOL_JAR_URL -O /usr/local/bin/apktool.jar && \  
sed -i '1s?#!/bin/bash?#!/bin/sh?' $APKTOOL_SCRIPT_PATH && \  
chmod +x /usr/local/bin/apktool* && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
apk del .build-dependencies  
  
ENV LANG=C.UTF-8  
CMD ["apktool", "-version"]  

