FROM centos:centos7  
  
RUN yum install -y java-1.7.0-openjdk-headless.x86_64 wget tar &&\  
yum clean all  
  
ENV nexus_version 2.11.4-01  
RUN cd /usr/local && \  
wget -qO-
"http://download.sonatype.com/nexus/oss/nexus-${nexus_version}-bundle.tar.gz"
| tar xz && \  
ln -s "nexus-${nexus_version}" nexus && \  
rm -rf /usr/local/sonatype-work/nexus && \  
ln -s /nexus /usr/local/sonatype-work/nexus  
  
VOLUME /nexus  
  
EXPOSE 8081  
ENV CONTEXT_PATH /nexus  
  
CMD RUN_AS_USER=root NEXUS_CONTEXT_PATH=$CONTEXT_PATH
/usr/local/nexus/bin/nexus console  

