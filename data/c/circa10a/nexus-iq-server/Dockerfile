FROM centos:latest  
  
ENV IQ_VERSION 1.47.0-01  
ENV JAVA_HOME /opt/java  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 172  
ENV JAVA_VERSION_BUILD 11  
ENV SIG a58eab1ec242421181065cdc37240b08  
  
#update packages for security vulnerabilities  
RUN yum -y update && yum clean all  
  
# install Oracle JRE  
RUN mkdir -p /opt \  
&& curl --fail --silent --location --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie; " \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/"${SIG}"/server-
jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \  
| gunzip \  
| tar -x -C /opt \  
&& ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JAVA_HOME}  
  
ENV SONATYPE_WORK /sonatype-work  
  
RUN mkdir -p /opt/sonatype/iq-server \  
&& curl --fail --silent --location --retry 3 \  
https://download.sonatype.com/clm/server/nexus-iq-
server-${IQ_VERSION}-bundle.tar.gz \  
| gunzip \  
| tar x -C /opt/sonatype/iq-server nexus-iq-server-${IQ_VERSION}.jar
config.yml  
  
RUN useradd -r -u 201 -m -c "iq-server role account" -d ${SONATYPE_WORK} -s
/bin/false iq-server  
  
VOLUME ${SONATYPE_WORK}  
  
ENV JVM_OPTIONS -server  
EXPOSE 8070  
EXPOSE 8071  
WORKDIR /opt/sonatype/iq-server  
USER iq-server  
CMD ${JAVA_HOME}/bin/java \  
${JVM_OPTIONS} \  
-Ddw.sonatypeWork=${SONATYPE_WORK} \  
-jar nexus-iq-server-${IQ_VERSION}.jar \  
server config.yml  

