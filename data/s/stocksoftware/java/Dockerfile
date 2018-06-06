#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
# AlpineLinux with a glibc-2.23 and Oracle Java  
FROM alpine:3.4  
  
MAINTAINER Stock Software  
  
# Java Version and other ENV  
ENV JAVA_VERSION_MAJOR=7 \  
JAVA_VERSION_MINOR=80 \  
JAVA_VERSION_BUILD=15 \  
JAVA_PACKAGE=jdk \  
JAVA_HOME=/opt/jdk \  
PATH=${PATH}:/opt/jdk/bin \  
GLIBC_VERSION=2.23-r3 \  
LANG=C.UTF-8  
# Install Java. This differs from anapsix/docker-alpine-java in that it does
not delete /opt/jdk/jre/plugin  
# Add curl and ca-certificates as all downstream images make use of this  
# Add bash to ease manual inspection of images  
RUN apk upgrade --update && \  
apk add --update bash curl ca-certificates && \  
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
mkdir /opt && curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie"
-o /tmp/java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
gunzip /tmp/java.tar.gz && \  
tar -C /opt -xf /tmp/java.tar && \  
apk del glibc-i18n && \  
rm -rf /tmp/* /var/cache/apk/* && \  
ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk && \  
rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx*  
  
# Fix DNS resolution issues when nss is not installed  
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >
/etc/nsswitch.conf  
  
# Set DNS cache to 10 seconds (Cache is permanent by default). Network hosts
are volatile in Docker clusters.  
RUN grep '^networkaddress.cache.ttl='
${JAVA_HOME}/jre/lib/security/java.security || echo
'networkaddress.cache.ttl=10' >> ${JAVA_HOME}/jre/lib/security/java.security  
  
# Disable ipv6 as several apps do not work with it, and in a docker container
DNS failures occurs from within java apps.  
RUN echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.conf  

