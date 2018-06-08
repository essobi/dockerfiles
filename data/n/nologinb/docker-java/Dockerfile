FROM ubuntu:18.04  
ENV JAVA_VERSION=10.0.1 \  
JCE_VERSION=8 \  
JAVA_BUILD=10 \  
JAVA_PATH=fb4372174a714e6b8c52526dc134031e \  
JAVA_HOME="/usr/lib/jvm/default-jvm"  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install ca-certificates curl unzip -y --no-install-recommends  
  
RUN mkdir -p /usr/lib/jvm \  
&& curl --silent --location --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${JAVA_VERSION}"+"${JAVA_BUILD}"/"${JAVA_PATH}"/jdk-"${JAVA_VERSION}"_linux-x64_bin.tar.gz
\  
| tar xz -C /usr/lib/jvm \  
\  
&& ln -s "/usr/lib/jvm/jdk-${JAVA_VERSION}" "$JAVA_HOME" \  
&& rm -rf $JAVA_HOME/lib/src.zip \  
&& curl -o /tmp/jce_policy-${JCE_VERSION}.zip --silent --location --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jce/${JCE_VERSION}/jce_policy-${JCE_VERSION}.zip \  
&& unzip -jo -d "${JAVA_HOME}/lib/security" /tmp/jce_policy-${JCE_VERSION}.zip
\  
&& rm "${JAVA_HOME}/lib/security/README.txt" \  
&& apt-get autoclean && apt-get --purge -y autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JAVA_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JAVA_HOME}/bin/javaws" 1 && \  
update-alternatives --set java "${JAVA_HOME}/bin/java" && \  
update-alternatives --set javaws "${JAVA_HOME}/bin/javaws"

