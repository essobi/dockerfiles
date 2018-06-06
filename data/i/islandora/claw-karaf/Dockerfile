FROM islandora/claw-maven:open-jdk  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
EXPOSE 8181  
ARG KARAF_VERSION="4.0.5"  
ENV KARAF_HOME="/opt/karaf" \  
KARAF_OPTS="-Xms128M -Xmx512M -XX:+UnlockDiagnosticVMOptions
-XX:+UnsyncloadClass" \  
PATH=${PATH}:/opt/karaf/bin  
  
RUN addgroup -g 1000 karaf && \  
adduser -u 100 -s /sbin/nologin -G karaf -DH -h ${KARAF_HOME} karaf  
  
RUN apk-install openssh bash && \  
curl -L http://archive.apache.org/dist/karaf/${KARAF_VERSION}/apache-
karaf-${KARAF_VERSION}.tar.gz | \  
tar -xzf - -C /tmp && \  
mv /tmp/apache-karaf-${KARAF_VERSION} /opt/karaf && \  
cleanup  
  
COPY rootfs /  

