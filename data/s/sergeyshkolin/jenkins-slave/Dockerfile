FROM ubuntu:16.04  
  
ENV SWARM_VERSION=2.2 \  
MAVEN_VERSION=3.3.9 \  
JAVA_VERSION_MAJOR=8 \  
JAVA_VERSION_MINOR=121 \  
JAVA_VERSION_BUILD=13 \  
JAVA_PACKAGE=jdk \  
JAVA_HOME=/opt/jdk \  
PATH=${PATH}:/opt/jdk/bin \  
MAVEN_HOME=/opt/maven \  
GRADLE_VERSION=3.4.1  
  
# Additional packages  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
software-properties-common \  
curl \  
wget \  
git \  
gitstats \  
rpl \  
unzip \  
openssh-client \  
iproute2  
  
# Download and unarchive maven  
RUN wget --no-verbose -O /tmp/apache-maven-${MAVEN_VERSION}.tar.gz
http://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& tar xzf /tmp/apache-maven-3.3.9.tar.gz -C /opt/ \  
&& ln -s /opt/apache-maven-3.3.9 /opt/maven \  
&& ln -s /opt/maven/bin/mvn /usr/local/bin \  
&& rm -f /tmp/apache-maven-3.3.9.tar.gz  
  
# Download and unarchive gradle  
RUN curl -L https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-
all.zip > /usr/share/gradle-$GRADLE_VERSION-all.zip \  
&& unzip -d /usr/share/ /usr/share/gradle-$GRADLE_VERSION-all.zip \  
&& ln -s /usr/share/gradle-$GRADLE_VERSION /usr/share/gradle \  
&& rm /usr/share/gradle-$GRADLE_VERSION-all.zip \  
&& ln -s /usr/share/gradle/bin/gradle /usr/bin/gradle  
  
# Download and unarchive Java  
RUN curl -kLOH "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/e9e7ea248e2c4826b92b3f075a80e441/${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz
\  
&& gunzip
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \  
&& tar -xf
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar -C
/opt \  
&& rm
${JAVA_PACKAGE}-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar \  
&& ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} /opt/jdk \  
&& rm -rf /opt/jdk/*src.zip \  
/opt/jdk/lib/missioncontrol \  
/opt/jdk/lib/visualvm \  
/opt/jdk/lib/*javafx* \  
/opt/jdk/jre/lib/plugin.jar \  
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
/opt/jdk/jre/lib/amd64/libjfx*.so \  
&& mkdir -p /opt/jdk/jre/lib/security \  
# Download Java Cryptography Extension  
&& curl -s -k -L -C - -b "oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jce/${JAVA_VERSION_MAJOR}/jce_policy-${JAVA_VERSION_MAJOR}.zip >
/tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip \  
&& unzip -d /tmp/ /tmp/jce_policy-${JAVA_VERSION_MAJOR}.zip \  
&& yes |cp -v /tmp/UnlimitedJCEPolicyJDK${JAVA_VERSION_MAJOR}/*.jar
/opt/jdk/jre/lib/security/ \  
&& rm -fr /tmp/* \  
&& apt-get -y autoremove \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
# Jenkins user  
RUN groupadd jenkins && \  
useradd -d /home/jenkins -s /bin/bash -m jenkins -g jenkins  
  
# Swarm client  
RUN wget -O /home/jenkins/swarm-client.jar http://repo.jenkins-
ci.org/releases/org/jenkins-ci/plugins/swarm-client/${SWARM_VERSION}/swarm-
client-${SWARM_VERSION}-jar-with-dependencies.jar  
  
ADD jenkins-slave-run.sh /  
  
CMD ["/jenkins-slave-run.sh"]  
  

