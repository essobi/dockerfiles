FROM frolvlad/alpine-glibc:alpine-3.7  
  
MAINTAINER dockerfiles@nearpod.com  
  
WORKDIR /usr/local  
  
ENV LANG="C.UTF-8"  
  
ARG ZULU_ARCH=zulu8.25.0.1-jdk8.0.152-linux_x64  
ARG ZULU_MD5=cc6e9ff13c27d27033220208d5450f2d  
ARG JAVA_HOME=/usr/local/lib/jvm/$ZULU_ARCH  
ENV JAVA_HOME=$JAVA_HOME  
ENV PATH=$PATH:$JAVA_HOME/bin  
  
RUN set -ex; \  
WORKDIR=$PWD; \  
apk --no-cache add ca-certificates curl bash; \  
mkdir -p "$JAVA_HOME"; \  
curl -q -sSLO "http://cdn.azul.com/zulu/bin/${ZULU_ARCH}.tar.gz"; \  
echo "$ZULU_MD5 ${ZULU_ARCH}.tar.gz" | md5sum -c; \  
tar -xzf "${ZULU_ARCH}.tar.gz" \--strip-components=1 -C "$JAVA_HOME"; \  
rm -rf "${ZULU_ARCH}.tar.gz" "$JAVA_HOME/demo" "$JAVA_HOME/man"
"$JAVA_HOME/sample" "$JAVA_HOME/src.zip"; \  
java -version  

