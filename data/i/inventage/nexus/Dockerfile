FROM centos:centos7  
MAINTAINER Inventage <iii-team@inventage.com>  
  
ENV SONATYPE_WORK /sonatype-work  
ENV NEXUS_VERSION 3.0.0-b2016011501  
  
ENV JAVA_HOME /opt/java  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 74  
ENV JAVA_VERSION_BUILD 02  
RUN yum install -y \  
curl tar createrepo \  
&& yum clean all  
  
# install Oracle JRE  
RUN mkdir -p /opt \  
&& curl --fail --silent --location --retry 3 \  
\--header "Cookie: oraclelicense=accept-securebackup-cookie; " \  
http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-b${JAVA_VERSION_BUILD}/server-
jre-${JAVA_VERSION_MAJOR}u${JAVA_VERSION_MINOR}-linux-x64.tar.gz \  
| gunzip \  
| tar -x -C /opt \  
&& ln -s /opt/jdk1.${JAVA_VERSION_MAJOR}.0_${JAVA_VERSION_MINOR} ${JAVA_HOME}  
  
RUN curl --fail --silent --location --retry 3 \  
https://download.sonatype.com/nexus/3/nexus-${NEXUS_VERSION}-unix.tar.gz \  
| gunzip \  
| tar x -C /tmp nexus-${NEXUS_VERSION} \  
&& mkdir -p /opt/sonatype \  
&& mv /tmp/nexus-${NEXUS_VERSION} /opt/sonatype/nexus \  
&& echo "-include-options /tmp/nexus.vmoptions" >>
/opt/sonatype/nexus/bin/nexus.vmoptions  
  
RUN useradd -r -u 200 -m -c "nexus role account" -d ${SONATYPE_WORK} -s
/bin/false nexus \  
&& chown nexus:nexus /opt/sonatype/nexus/bin/nexus.vmoptions  
  
VOLUME ${SONATYPE_WORK}  
  
EXPOSE 8081  
WORKDIR /opt/sonatype/nexus  
USER nexus  
ENV CONTEXT_PATH /  
ENV MAX_HEAP 768m  
ENV MIN_HEAP 256m  
CMD echo "-server" > /tmp/nexus.vmoptions \  
&& echo "-Xms${MIN_HEAP}" >> /tmp/nexus.vmoptions \  
&& echo "-Xmx${MAX_HEAP}" >> /tmp/nexus.vmoptions \  
&& echo "-Dkaraf.data=${SONATYPE_WORK}" >> /tmp/nexus.vmoptions \  
&& echo "-Dkaraf.instances=${SONATYPE_WORK}/instances" >> /tmp/nexus.vmoptions
\  
&& echo "-Djava.io.tmpdir=${SONATYPE_WORK}/tmp" >> /tmp/nexus.vmoptions \  
&& exec bin/nexus run  

