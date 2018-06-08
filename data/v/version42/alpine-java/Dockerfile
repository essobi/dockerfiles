FROM version42/alpine-glibc:alpine3.7-glibc2.26r0  
MAINTAINER Joe Brutto  
  
# download & install Java  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=152 \  
JAVA_VERSION_BUILD=16 \  
JAVA_EXTRA_PATH=aa0333dd3019491ca4f6ddbe78cdb6d0 \  
JAVA_PACKAGE=jdk \  
JAVA_HOME=/opt/jdk \  
PATH=${PATH}:/opt/jdk/bin  
  
RUN \  
apk add --update curl && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \  
-o /tmp/java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_EXTRA_PATH}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
gunzip /tmp/java.tar.gz && \  
tar -C /opt -xf /tmp/java.tar && \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" \  
-o /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip \  
http://download.oracle.com/otn-
pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip && \  
cd /tmp && unzip /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip && \  
cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar /opt/jdk/jre/lib/security && \  
sed -i s/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=10/
$JAVA_HOME/jre/lib/security/java.security && \  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/plugin \  
/opt/jdk/jre/bin/javaws \  
/opt/jdk/jre/bin/jjs \  
/opt/jdk/jre/bin/orbd \  
/opt/jdk/jre/bin/pack200 \  
/opt/jdk/jre/bin/policytool \  
/opt/jdk/jre/bin/rmid \  
/opt/jdk/jre/bin/rmiregistry \  
/opt/jdk/jre/bin/servertool \  
/opt/jdk/jre/bin/tnameserv \  
/opt/jdk/jre/bin/unpack200 \  
/opt/jdk/jre/lib/javaws.jar \  
/opt/jdk/jre/lib/deploy* \  
/opt/jdk/jre/lib/desktop \  
/opt/jdk/jre/lib/*javafx* \  
/opt/jdk/jre/lib/*jfx* \  
/opt/jdk/jre/lib/amd64/libdecora_sse.so \  
/opt/jdk/jre/lib/amd64/libprism_*.so \  
/opt/jdk/jre/lib/amd64/libfxplugins.so \  
/opt/jdk/jre/lib/amd64/libglass.so \  
/opt/jdk/jre/lib/amd64/libgstreamer-lite.so \  
/opt/jdk/jre/lib/amd64/libjavafx*.so \  
/opt/jdk/jre/lib/amd64/libjfx*.so \  
/opt/jdk/jre/lib/ext/jfxrt.jar \  
/opt/jdk/jre/lib/ext/nashorn.jar \  
/opt/jdk/jre/lib/oblique-fonts \  
/opt/jdk/jre/lib/plugin.jar \  
/tmp/* /var/cache/apk/* && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  

