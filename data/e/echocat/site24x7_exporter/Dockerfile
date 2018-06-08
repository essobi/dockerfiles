FROM alpine:3.4  
MAINTAINER contact@echocat.org  
  
# Prepare build environment  
ENV LANG C.UTF-8  
RUN apk update \  
&& apk add --no-cache bash go openjdk8  
COPY . /tmp/buildroot/site24x7_exporter  
  
# Build exporter  
RUN cd /tmp/buildroot/site24x7_exporter \  
&& export GOROOT=/usr/lib/go \  
&& export JAVA_HOME=/usr/lib/jvm/default-jvm \  
&& chmod +x /tmp/buildroot/site24x7_exporter/gradlew \  
&& ./gradlew --stacktrace --info -Dplatforms=linux-amd64 build \  
&& cp /tmp/buildroot/site24x7_exporter/build/out/site24x7_exporter-linux-amd64
/usr/bin/site24x7_exporter \  
&& chmod +x /usr/bin/site24x7_exporter  
  
# Clean up build environment  
RUN apk del \  
bash readline ncurses-libs ncurses-terminfo ncurses-terminfo-base \  
go \  
libffi libtasn1 p11-kit p11-kit-trust ca-certificates java-cacerts libxau
libxdmcp libxcb libx11 libxi libxrender libxtst libpng freetype libgcc giflib
openjdk8-jre-lib java-common alsa-lib openjdk8-jre-base openjdk8-jre openjdk8
\  
&& rm -rf /var/cache/* \  
&& rm -rf /root/.go \  
&& rm -rf /root/.gradle \  
&& rm -rf /media \  
&& rm -rf /tmp/*  
  
ENTRYPOINT ["/usr/bin/site24x7_exporter"]  

