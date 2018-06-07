FROM node:alpine  
  
# Install CURL  
RUN apk add --update curl && \  
rm -rf /var/cache/apk/*  
  
  
# Java Version and other ENV  
ENV JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=45 \  
JAVA_VERSION_BUILD=14 \  
JAVA_PACKAGE=jdk \  
JAVA_JCE="limited" \  
JAVA_HOME=/opt/jdk \  
PATH=${PATH}:/opt/jdk/bin \  
GLIBC_VERSION=2.23-r3 \  
LANG=C.UTF-8  
  
ENV JVM_URL=http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz  
  
# do all in one step  
RUN set -ex && \  
apk upgrade --update && \  
apk add --update libstdc++ curl ca-certificates bash && \  
for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION}
glibc-i18n-${GLIBC_VERSION}; do curl -sSL https://github.com/andyshinn/alpine-
pkg-glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk;
done && \  
apk add --allow-untrusted /tmp/*.apk && \  
rm -v /tmp/*.apk && \  
( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true ) && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \  
mkdir /opt && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/java.tar.gz \  
${JVM_URL} && \  
gunzip /tmp/java.tar.gz && \  
tar -C /opt -xf /tmp/java.tar && \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
if [ "${JAVA_JCE}" == "unlimited" ]; then echo "Installing Unlimited JCE
policy" >&2 && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip \  
http://download.oracle.com/otn-
pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip && \  
cd /tmp && unzip /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip && \  
cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar /opt/jdk/jre/lib/security; \  
fi && \  
sed -i s/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=10/
$JAVA_HOME/jre/lib/security/java.security && \  
apk del curl glibc-i18n && \  
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
  
RUN java -version  
  
#  
# Install Atlassian SKD  
#  
  
ENV ATLS_VERSIN 6.2.14  
ENV ATLS_SHA512
48ad1d0c8ee725ee0e6753231e061ac04da54167797429d39ed8a4815b6705d0fc643794bf767809d819fc22039fe8923e8a94bb9aa3bf2a6e32a25f53039153  
  
#  
# BASE PACKAGES + DOWNLOAD GLIBC & ORACLE JAVA & ATLASSIAN SDK  
#  
RUN apk add --no-cache \  
bash \  
ca-certificates \  
curl \  
gzip \  
tar && \  
mkdir -p /opt/atlas/ && \  
mkdir -p /opt/atlas-work/ && \  
echo "=== INSTALLING ATLASSIAN SDK==================" && \  
echo "${ATLS_SHA512} /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz" >
/opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz.sha512 && \  
curl -jkSL -o /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz \  
https://maven.atlassian.com/content/repositories/atlassian-
public/com/atlassian/amps/atlassian-plugin-sdk/${ATLS_VERSIN}/atlassian-
plugin-sdk-${ATLS_VERSIN}.tar.gz && \  
sha512sum -c /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz.sha512  
  
  
#  
# INSTALL AND CONFIGURE  
#  
COPY docker-entrypoint.sh /opt/docker-entrypoint.sh  
RUN chmod u+rx,g+rx,o+rx,a-w /opt/docker-entrypoint.sh && \  
addgroup -g 10777 worker && \  
adduser -D -G worker -u 10777 worker && \  
chown -R worker:worker /opt/atlas/ && \  
chmod -R u+rwx,g+rwx,o-rwx /opt/atlas/ && \  
chown -R worker:worker /opt/atlas-work/ && \  
chmod -R u+rwx,g+rwx,o-rwx /opt/atlas-work/ && \  
tar -C /opt -xf /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz && \  
chown -R worker:root /opt/atlassian-plugin-sdk-${ATLS_VERSIN} && \  
rm -f /opt/atlassian-plugin-sdk-${ATLS_VERSIN}.tar.gz && \  
apk del gzip tar && \  
rm -rf /tmp/* /var/cache/apk/*  
  
#  
# RUN  
#  
EXPOSE 2990  
USER worker  
ENV MAVEN_REPOSITORY_MIRROR "false"  
ENV JAVA_HOME /opt/jdk  
ENV PATH ${PATH}:/opt/atlassian-plugin-
sdk-${ATLS_VERSIN}/bin/:/opt/jdk/bin/:/usr/bin/curl/  
WORKDIR /opt/atlas/  
VOLUME ["/opt/atlas/"]  
ENTRYPOINT ["/opt/docker-entrypoint.sh"]  
CMD ["atlas-version"]

