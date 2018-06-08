# Dockerfile for scottabernethy/java JDK 7  
FROM scottabernethy/debian  
  
ENV JAVA_VERSION 7  
ENV JAVA_UPDATE 79  
ENV JAVA_BUILD 15  
  
ENV JAVA_HOME /usr/lib/jvm/jdk1.${JAVA_VERSION}.0_${JAVA_UPDATE}  
  
RUN \  
curl -o /tmp/download.tar.gz \  
\--silent --location --retry 3 \  
\--cacert /etc/ssl/certs/GeoTrust_Global_CA.pem \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie;" \  
http://download.oracle.com/otn-
pub/java/jdk/"${JAVA_VERSION}"u"${JAVA_UPDATE}"-b"${JAVA_BUILD}"/jdk-"${JAVA_VERSION}"u"${JAVA_UPDATE}"-linux-x64.tar.gz
&& \  
echo "9222e097e624800fdd9bfb568169ccad /tmp/download.tar.gz" | md5sum --check
&& \  
mkdir -p /usr/lib/jvm && \  
tar -xzf /tmp/download.tar.gz -C /usr/lib/jvm && \  
rm /tmp/download.tar.gz && \  
rm -r "${JAVA_HOME}"/lib/missioncontrol && \  
rm -r "${JAVA_HOME}"/lib/visualvm && \  
rm "${JAVA_HOME}"/src.zip  
  
RUN \  
update-alternatives --install "/usr/bin/java" "java" "${JAVA_HOME}/bin/java" 1
&& \  
update-alternatives --install "/usr/bin/javaws" "javaws"
"${JAVA_HOME}/bin/javaws" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1 && \  
update-alternatives --set java "${JAVA_HOME}/bin/java" && \  
update-alternatives --set javaws "${JAVA_HOME}/bin/javaws" && \  
update-alternatives --set javac "${JAVA_HOME}/bin/javac"  

