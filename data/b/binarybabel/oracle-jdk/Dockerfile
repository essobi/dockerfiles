#######################################################################  
# IMPORTANT: This is just one Dockerfile varient in a build sequence! #  
# #  
# Dockerfiles for each distribution can be viewed on GitHub: #  
# https://github.com/binarybabel/docker-jdk/tree/master/src #  
# #  
#######################################################################  
  
FROM alpine  
MAINTAINER BinaryBabel OSS <oss@binarybabel.org>  
  
RUN apk --update add curl ca-certificates tar \  
&& curl -Ls https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.23-r3/glibc-2.23-r3.apk > /tmp/glibc-2.23-r3.apk \  
&& apk add --allow-untrusted /tmp/glibc-2.23-r3.apk  
  
ENV JAVA_DOWNLOAD=http://download.oracle.com/otn-
pub/java/jdk/8u171-b11/512cd62ec5174c3487ac17c61aaa89e8/jdk-8u171-linux-x64.tar.gz  
RUN mkdir -p /opt && curl -jfksSLH "Cookie: oraclelicense=accept-securebackup-
cookie" \  
"${JAVA_DOWNLOAD:-$(curl -s https://lv.binarybabel.org/catalog-
api/java/jdk8.txt?p=downloads.tgz)}" \  
| tar -xzf - -C /opt \  
&& ln -s /opt/jdk1.*.0_* /opt/jdk \  
&& rm -rf /opt/jdk/*src.zip \  
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
/opt/jdk/jre/lib/amd64/libjfx*.so  
  
ENV JAVA_HOME /opt/jdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
COPY java.sh /usr/bin/java  
RUN chmod 755 /usr/bin/java  
ENTRYPOINT ["/usr/bin/java"]  
CMD ["-version"]  
WORKDIR /srv  

