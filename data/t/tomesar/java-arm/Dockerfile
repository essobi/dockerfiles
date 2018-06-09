FROM tomesar/armv7hf-debian-qemu  
  
RUN [ "cross-build-start" ]  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
bzip2 \  
unzip \  
xz-utils \  
curl \  
&& rm -rf /var/lib/apt/lists/  
  
RUN echo 'deb http://deb.debian.org/debian jessie-backports main' >
/etc/apt/sources.list.d/jessie-backports.list  
  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-armhf  
  
ENV JAVA_VERSION 8u121  
ENV JAVA_DEBIAN_VERSION 8u121-b13-1~bpo8+1  
ENV CA_CERTIFICATES_JAVA_VERSION 20161107~bpo8+1  
RUN mkdir -p /usr/share/man/man1  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y -t jessie-backports \  
openjdk-8-jdk="$JAVA_DEBIAN_VERSION" \  
librxtx-java \  
maven \  
ca-certificates-java=$CA_CERTIFICATES_JAVA_VERSION && rm -rf
/var/lib/apt/lists/* \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
RUN mkdir /app  
  
WORKDIR /app  
  
ADD run.sh /app/run.sh  
RUN chmod +x /app/run.sh  
  
CMD ["/app/run.sh"]  
  
RUN [ "cross-build-end" ]  

