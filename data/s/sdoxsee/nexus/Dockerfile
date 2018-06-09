FROM sonatype/nexus:2.13.0-01  
MAINTAINER Stephen Doxsee  
  
USER root  
  
RUN yum install -y unzip \  
yum clean all  
  
# install nexus-unpack-plugin  
RUN curl --fail --silent --location --retry 3 \  
-o /tmp/nexus-unpack-plugin-${NEXUS_VERSION}-bundle.zip \  
https://repo1.maven.org/maven2/org/sonatype/nexus/plugins/nexus-unpack-
plugin/${NEXUS_VERSION}/nexus-unpack-plugin-${NEXUS_VERSION}-bundle.zip \  
&& unzip -d /opt/sonatype/nexus/nexus/WEB-INF/plugin-repository \  
/tmp/nexus-unpack-plugin-${NEXUS_VERSION}-bundle.zip \  
&& find /opt/sonatype/nexus/nexus/WEB-INF/plugin-repository/nexus-unpack-
plugin-${NEXUS_VERSION} \  
-type d -exec chmod 755 {} \; \  
&& find /opt/sonatype/nexus/nexus/WEB-INF/plugin-repository/nexus-unpack-
plugin-${NEXUS_VERSION} \  
-type f -exec chmod 644 {} \; \  
&& rm /tmp/nexus-unpack-plugin-${NEXUS_VERSION}-bundle.zip  
  
USER nexus  

