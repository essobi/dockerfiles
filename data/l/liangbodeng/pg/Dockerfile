FROM centos:centos6  
  
ENV JAVA_HOME /usr/java/default  
ENV FLYWAY_VERSION 4.0.3  
ENV UID 1000  
  
RUN \  
yum -y install sudo wget unzip && \  
useradd -m eng -u ${UID} && \  
echo "eng ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
wget --no-cookies \  
\--no-check-certificate \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/6u45-b06/jre-6u45-linux-x64-rpm.bin" \  
-O /tmp/jre-6u45-linux-x64-rpm.bin && \  
chmod a+x /tmp/jre-6u45-linux-x64-rpm.bin && \  
/tmp/jre-6u45-linux-x64-rpm.bin -x && \  
rm /tmp/jre-6u45-linux-x64-rpm.bin && \  
yum -y localinstall /jre-6u45-linux-amd64.rpm && \  
rm /jre-6u45-linux-amd64.rpm && \  
yum clean all && \  
wget --no-cookies \  
\--no-check-certificate \  
"http://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.zip" \  
-O /tmp/flyway.zip && \  
unzip /tmp/flyway.zip && \  
rm /tmp/flyway.zip && \  
mkdir -p /opt/arin/ddl && \  
mv /flyway-${FLYWAY_VERSION} /opt/arin/flyway && \  
mv /opt/arin/flyway/conf/flyway.conf /opt/arin/flyway/conf/flyway.conf.bak &&
\  
chmod +x /opt/arin/flyway/flyway && \  
ln -s /opt/arin/flyway/flyway /usr/local/bin/flyway  
  
ADD ./flyway.conf /opt/arin/flyway/conf/flyway.conf  
  
VOLUME /opt/arin/pg-portable  
  
WORKDIR /opt/arin/pg-portable  
  
USER eng  
CMD []  

