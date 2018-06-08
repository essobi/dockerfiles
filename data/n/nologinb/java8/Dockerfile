FROM ubuntu:17.10  
ENV JAVA_VERSION=8 \  
JAVA_UPDATE=162 \  
JAVA_BUILD=12 \  
JAVA_PATH=0da788060d494f5095bf8624735fa2f1 \  
JAVA_HOME="/usr/lib/jvm/default-jvm"  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install ca-certificates curl unzip -y --no-install-recommends  
  
RUN mkdir -p /usr/lib/jvm \  
&& curl --silent --location --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${JAVA_VERSION}"u"${JAVA_UPDATE}"-b"${JAVA_BUILD}"/"${JAVA_PATH}"/jdk-"${JAVA_VERSION}"u"${JAVA_UPDATE}"-linux-x64.tar.gz
\  
| tar xz -C /usr/lib/jvm \  
&& ln -s "/usr/lib/jvm/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}" "$JAVA_HOME" \  
&& rm -rf "$JAVA_HOME/"*src.zip \  
&& rm -rf "$JAVA_HOME/lib/missioncontrol" \  
"$JAVA_HOME/lib/visualvm" \  
"$JAVA_HOME/lib/"*javafx* \  
"$JAVA_HOME/jre/lib/plugin.jar" \  
"$JAVA_HOME/jre/lib/ext/jfxrt.jar" \  
"$JAVA_HOME/jre/bin/javaws" \  
"$JAVA_HOME/jre/lib/javaws.jar" \  
"$JAVA_HOME/jre/lib/desktop" \  
"$JAVA_HOME/jre/plugin" \  
"$JAVA_HOME/jre/lib/"deploy* \  
"$JAVA_HOME/jre/lib/"*javafx* \  
"$JAVA_HOME/jre/lib/"*jfx* \  
"$JAVA_HOME/jre/lib/amd64/libdecora_sse.so" \  
"$JAVA_HOME/jre/lib/amd64/"libprism_*.so \  
"$JAVA_HOME/jre/lib/amd64/libfxplugins.so" \  
"$JAVA_HOME/jre/lib/amd64/libglass.so" \  
"$JAVA_HOME/jre/lib/amd64/libgstreamer-lite.so" \  
"$JAVA_HOME/jre/lib/amd64/"libjavafx*.so \  
"$JAVA_HOME/jre/lib/amd64/"libjfx*.so \  
&& curl -o /tmp/jce_policy-${JAVA_VERSION}.zip --silent --location --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jce/${JAVA_VERSION}/jce_policy-${JAVA_VERSION}.zip \  
&& unzip -jo -d "${JAVA_HOME}/jre/lib/security"
/tmp/jce_policy-${JAVA_VERSION}.zip \  
&& rm "${JAVA_HOME}/jre/lib/security/README.txt" \  
&& apt-get autoclean && apt-get --purge -y autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JAVA_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JAVA_HOME}/bin/javaws" 1 && \  
update-alternatives --set java "${JAVA_HOME}/bin/java" && \  
update-alternatives --set javaws "${JAVA_HOME}/bin/javaws"  

