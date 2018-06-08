FROM alpine:3.3  
RUN apk add -U libc6-compat wget sudo openssh-client git bash python py-pip
py-crypto \  
&& wget -O /tmp/glibc.apk "https://circle-artifacts.com/gh/andyshinn/alpine-
pkg-glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk" \  
&& apk add --allow-untrusted /tmp/glibc.apk \  
&& /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib \  
&& rm /tmp/glibc.apk \  
&& rm -rf /var/cache/apk/*  
  
# Java  
ENV JAVA_VERSION=8 \  
JAVA_UPDATE=66 \  
JAVA_BUILD=17 \  
JAVA_HOME=/usr/lib/jvm/default-jvm \  
JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8  
  
RUN apk add --update wget ca-certificates \  
&& cd /tmp \  
&& wget --header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}u${JAVA_UPDATE}-b${JAVA_BUILD}/jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz"
\  
&& tar xzf "jdk-${JAVA_VERSION}u${JAVA_UPDATE}-linux-x64.tar.gz" \  
&& mkdir -p "/usr/lib/jvm" \  
&& mv "/tmp/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}"
"/usr/lib/jvm/java-${JAVA_VERSION}-oracle" \  
&& ln -s "java-${JAVA_VERSION}-oracle" "$JAVA_HOME" \  
&& ln -s "$JAVA_HOME/bin/"* "/usr/bin/" \  
&& rm -rf "$JAVA_HOME/"*src.zip \  
rm -rf "$JAVA_HOME/lib/missioncontrol" \  
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
&& apk del wget ca-certificates \  
&& rm /tmp/* /var/cache/apk/* \  
&& echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
# Ansible  
RUN pip install --upgrade pip==8.0.2 \  
&& pip install ansible==2.0.0.2  
  
# Rundeck  
RUN mkdir /rundeck \  
&& wget -O /rundeck/rundeck-launcher.jar
"http://dl.bintray.com/rundeck/rundeck-maven/rundeck-launcher-2.6.2.jar"  
  
COPY ./entrypoint.sh /entrypoint.sh  
COPY ./rundeck-config.properties /rundeck/server/config/rundeck-
custom.properties  
  
ENV RUNDECK_BASE=/rundeck \  
RUNDECK_WEB_CONTEXT=/ \  
RUNDECK_USER_NAME=admin \  
RUNDECK_USER_PASSWORD=admin \  
RUNDECK_SERVER_URL=http://localhost:4440 \  
RUNDECK_DB_USERNAME=rundeck \  
RUNDECK_DB_PASSWORD=rundeck \  
RUNDECK_DB_HOST=mysql \  
RUNDECK_DB_PORT=3306  
EXPOSE 4440  
VOLUME [ "/rundeck/var/storage/content/keys", "/rundeck/projects" ]  
  
WORKDIR "/rundeck"  
  
ENTRYPOINT ["/bin/bash"]  
CMD [ "/entrypoint.sh" ]  

