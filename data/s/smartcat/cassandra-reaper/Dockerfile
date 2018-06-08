FROM anapsix/alpine-java:8_server-jre  
  
MAINTAINER Matija Gobec <matija.gobec@smartcat.io>  
  
ENV BUILD_JAVA_VERSION_MAJOR=8 \  
BUILD_JAVA_VERSION_MINOR=92 \  
BUILD_JAVA_VERSION_BUILD=14 \  
BUILD_JAVA_PACKAGE=jdk \  
BUILD_JAVA_JCE=standard \  
BUILD_JAVA_HOME=/opt/build/jdk  
  
RUN apk upgrade \--update && \  
apk add \--update curl openssl && \  
mkdir /opt/build && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/java.tar.gz \  
http://download.oracle.com/otn-
pub/java/jdk/${BUILD_JAVA_VERSION_MAJOR}u${BUILD_JAVA_VERSION_MINOR}-b${BUILD_JAVA_VERSION_BUILD}/${BUILD_JAVA_PACKAGE}-${BUILD_JAVA_VERSION_MAJOR}u${BUILD_JAVA_VERSION_MINOR}-linux-x64.tar.gz
&& \  
gunzip /tmp/java.tar.gz && \  
tar -C /opt/build -xf /tmp/java.tar && \  
ln -s
/opt/build/jdk1.${BUILD_JAVA_VERSION_MAJOR}.0_${BUILD_JAVA_VERSION_MINOR}
/opt/build/jdk && \  
if [ "${BUILD_JAVA_JCE}" == "unlimited" ]; then echo "Installing Unlimited JCE
policy" >&2 && \  
curl -jksSLH "Cookie: oraclelicense=accept-securebackup-cookie" -o
/tmp/jce_policy-${BUILD_JAVA_VERSION_MAJOR}.zip \  
http://download.oracle.com/otn-
pub/java/jce/${BUILD_JAVA_VERSION_MAJOR}/jce_policy-${BUILD_JAVA_VERSION_MAJOR}.zip
&& \  
cd /tmp && unzip /tmp/jce_policy-${BUILD_JAVA_VERSION_MAJOR}.zip && \  
cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar /opt/build/jdk/jre/lib/security; \  
fi && \  
sed -i s/#networkaddress.cache.ttl=-1/networkaddress.cache.ttl=30/
$BUILD_JAVA_HOME/jre/lib/security/java.security && \  
curl -sS -o /tmp/apache-maven-3.3.9-bin.tar.gz http://www-
us.apache.org/dist/maven/maven-3/3.3.9/binaries/apache-maven-3.3.9-bin.tar.gz
&& \  
tar -C /opt/build -xzf /tmp/apache-maven-3.3.9-bin.tar.gz && \  
wget -P /tmp https://github.com/thelastpickle/cassandra-
reaper/archive/0.4.1.zip && \  
unzip /tmp/0.4.1.zip -d /opt/build -q && \  
cd /opt/build/cassandra-reaper-0.4.1 && \  
export JAVA_HOME=/opt/build/jdk ; \  
export PATH=/opt/build/jdk/bin:${PATH} ; \  
/opt/build/apache-maven-3.3.9/bin/mvn \--batch-mode -Dmaven.test.skip=true
package && \  
mkdir /opt/cassandra-reaper && \  
cp /opt/build/cassandra-reaper-0.4.1/target/cassandra-reaper*.jar
/opt/cassandra-reaper/cassandra-reaper.jar && \  
apk del curl openssl && \  
rm -rf /opt/build /tmp/* /var/cache/apk/* /root/.m2  
  
COPY [\  
"./cassandra-reaper.yaml",\  
"./run-reaper.sh",\  
"/opt/cassandra-reaper/"\  
]  
RUN chmod -R 775 /opt/cassandra-reaper  
  
WORKDIR /opt/cassandra-reaper  
  
EXPOSE 8090 8091  
  
ENTRYPOINT ["./run-reaper.sh"]  

