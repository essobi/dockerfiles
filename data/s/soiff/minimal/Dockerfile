FROM soiff/bash:latest  
  
MAINTAINER 张仪 <wittcnezh@foxmail.coms>  
  
ENV GLIBC_PKG_VERSION=2.23-r3
GLIBC_DOWNLOAD_PREFIX=https://github.com/sgerrand/alpine-pkg-
glibc/releases/download  
RUN apk add \--no-cache --update-cache curl ca-certificates bash && \  
curl -Lo /etc/apk/keys/sgerrand.rsa.pub
"${GLIBC_DOWNLOAD_PREFIX}/${GLIBC_PKG_VERSION}/sgerrand.rsa.pub" && \  
curl -Lo glibc-${GLIBC_PKG_VERSION}.apk
"${GLIBC_DOWNLOAD_PREFIX}/${GLIBC_PKG_VERSION}/glibc-${GLIBC_PKG_VERSION}.apk"
&& \  
curl -Lo glibc-bin-${GLIBC_PKG_VERSION}.apk
"${GLIBC_DOWNLOAD_PREFIX}/${GLIBC_PKG_VERSION}/glibc-
bin-${GLIBC_PKG_VERSION}.apk" && \  
curl -Lo glibc-i18n-${GLIBC_PKG_VERSION}.apk
"${GLIBC_DOWNLOAD_PREFIX}/${GLIBC_PKG_VERSION}/glibc-i18n-${GLIBC_PKG_VERSION}.apk"
&& \  
apk add glibc-${GLIBC_PKG_VERSION}.apk glibc-bin-${GLIBC_PKG_VERSION}.apk
glibc-i18n-${GLIBC_PKG_VERSION}.apk  
  

