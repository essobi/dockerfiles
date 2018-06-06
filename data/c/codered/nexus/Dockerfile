FROM codered/ubuntu-java8  
  
MAINTAINER Ronan Gill <ronan.gill@code.red>  
  
ADD http://download.sonatype.com/nexus/oss/nexus-2.12.0-01-bundle.tar.gz
/u01/nexus-2.12.0-01-bundle.tar.gz  
  
RUN groupadd --gid 1009 nexus && \  
useradd --system --uid 1008 --gid 1009 --home-dir /u01/sonatype-nexus nexus &&
\  
mkdir -p /u01/sonatype-nexus /u01/sonatype-work && \  
tar -xzf /u01/nexus-2.12.0-01-bundle.tar.gz -C /u01/sonatype-nexus --strip-
components=1 && \  
rm /u01/nexus-2.12.0-01-bundle.tar.gz && \  
chown -R nexus\: /u01/sonatype-nexus /u01/sonatype-work  
  
VOLUME ["/u01/sonatype-work"]  
EXPOSE 8081  
USER nexus  
WORKDIR /u01/sonatype-nexus  
  
CMD /u01/sonatype-nexus/bin/nexus console  

