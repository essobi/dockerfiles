FROM pinterb/base:alpine  
  
MAINTAINER Brad Pinter <brad.pinter@gmail.com>  
  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 66  
ENV JAVA_VERSION_BUILD 17  
ENV JAVA_PACKAGE jdk  
  
RUN apk update && \  
apk add --update wget ca-certificates tar && \  
apk add --update bash openssh-client sudo && \  
wget -q "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk" && \  
apk add --allow-untrusted glibc-2.21-r2.apk && \  
mkdir /opt && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
| tar -xzf - -C /opt && \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/lib/plugin.jar \  
/opt/jdk/jre/lib/ext/jfxrt.jar \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/lib/javaws.jar \  
/opt/jdk/jre/lib/desktop \  
/opt/jdk/jre/plugin \  
/opt/jdk/jre/lib/deploy* \  
/opt/jdk/jre/lib/*javafx* \  
/opt/jdk/jre/lib/*jfx* \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so && \  
apk del --purge wget ca-certificates && \  
rm -rf /var/cache/apk/*  
  
ENV JAVA_HOME /opt/jdk  
ENV PATH $PATH:${JAVA_HOME}/bin  
  
RUN addgroup dev && \  
adduser -G dev dev -D -h /home/dev && \  
mkdir -p /home/dev/bin /home/dev/lib /home/dev/include /home/dev/.ssh && \  
sed -ri 's/(wheel:x:10:root)/\1,dev/' /etc/group && \  
sed -ri 's/# %wheel ALL=\\(ALL\\) NOPASSWD: ALL/%wheel ALL=\\(ALL\\) NOPASSWD:
ALL/' /etc/sudoers  
  
ENV PATH /home/dev/bin:$PATH  
  
RUN ssh-keygen -t rsa -N '' -f /home/dev/.ssh/dummy_rsa && \  
chown -R dev:dev /home/dev/.ssh  
  
# Create a shared data volume  
# We need to create an empty file, otherwise the volume will  
# belong to root.  
RUN mkdir /data/ /ops/ /state/  
RUN touch /data/.extra /ops/.extra /state/.extra  
RUN chown -R dev:dev /data  
RUN chown -R dev:dev /ops  
RUN chown -R dev:dev /state  
  
## Expose some volumes  
VOLUME ["/data", "/ops", "/state", "/home/dev/.ssh"]  
  
ENV HOME /home/dev  
USER dev  
WORKDIR /data  
  

