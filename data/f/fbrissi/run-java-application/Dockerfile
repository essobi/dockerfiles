FROM centos:latest  
  
MAINTAINER Filipe Bojikian Rissi <filiperissi@finchsolucoes.com.br>  
  
ARG gp=8080  
  
ENV JAVA_VERSION_MAJOR=9 \  
JAVA_VERSION_MINOR=0.4 \  
JAVA_VERSION_BUILD=11 \  
JAVA_PACKAGE=jdk \  
JAVA_HASH=c2514751926b4512b076cc82f959763f \  
JAVA_HOME=/opt/java \  
PATH=${PATH}:/opt/java/bin \  
JAVA_OPTS="" \  
LANG=en_US.UTF-8  
  
# Instalar Java  
  
RUN yum update -y \  
&& yum install -y which zip unzip \  
&& curl -jkSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}.${JAVA_VERSION_MINOR}+${JAVA_VERSION_BUILD}/${JAVA_HASH}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}.${JAVA_VERSION_MINOR}_linux-x64_bin.tar.gz
\  
&& tar -C /opt -zxf /tmp/java.tar.gz \  
&& ln -s /opt/jdk-${JAVA_VERSION_MAJOR}.${JAVA_VERSION_MINOR} ${JAVA_HOME} \  
&& rm -rf ${JAVA_HOME}/*src.zip \  
${JAVA_HOME}/lib/missioncontrol \  
${JAVA_HOME}/lib/visualvm \  
${JAVA_HOME}/lib/*javafx* \  
${JAVA_HOME}/plugin \  
${JAVA_HOME}/bin/javaws \  
${JAVA_HOME}/bin/jjs \  
${JAVA_HOME}/bin/keytool \  
${JAVA_HOME}/bin/orbd \  
${JAVA_HOME}/bin/pack200 \  
${JAVA_HOME}/bin/policytool \  
${JAVA_HOME}/bin/rmid \  
${JAVA_HOME}/bin/rmiregistry \  
${JAVA_HOME}/bin/servertool \  
${JAVA_HOME}/bin/tnameserv \  
${JAVA_HOME}/bin/unpack200 \  
${JAVA_HOME}/lib/javaws.jar \  
${JAVA_HOME}/lib/deploy* \  
${JAVA_HOME}/lib/desktop \  
${JAVA_HOME}/lib/*javafx* \  
${JAVA_HOME}/lib/*jfx* \  
${JAVA_HOME}/lib/amd64/libdecora_sse.so \  
${JAVA_HOME}/lib/amd64/libprism_*.so \  
${JAVA_HOME}/lib/amd64/libfxplugins.so \  
${JAVA_HOME}/lib/amd64/libglass.so \  
${JAVA_HOME}/lib/amd64/libgstreamer-lite.so \  
${JAVA_HOME}/lib/amd64/libjavafx*.so \  
${JAVA_HOME}/lib/amd64/libjfx*.so \  
${JAVA_HOME}/lib/ext/jfxrt.jar \  
${JAVA_HOME}/lib/ext/nashorn.jar \  
${JAVA_HOME}/jre/lib/oblique-fonts \  
${JAVA_HOME}/jre/lib/plugin.jar \  
/tmp/* /var/cache/apk/*  
  
RUN yum remove -y zip unzip \  
&& yum autoremove -y \  
&& yum clean all \  
&& rm -rf /tmp/* /var/tmp/*  
  
COPY entrypoint.sh /usr/bin/entrypoint  
COPY start.vmoptions .  
  
RUN chmod +x /usr/bin/entrypoint  
  
EXPOSE $gp  
  
ENTRYPOINT ["entrypoint"]  
CMD ["--server.port=$gp"]  

