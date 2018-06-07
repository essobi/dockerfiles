FROM centos:7  
LABEL maintainer="Tim Dudgeon<tdudgeon@informaticsmatters.com>"  
  
RUN yum update -y &&\  
yum install -y --setopt=tsflags=nodocs
--setopt=override_install_langs=en_US.utf8\  
docker-client\  
java-1.8.0-openjdk-headless &&\  
yum clean -y all &&\  
rm -rf /var/cache/yum  
  
ENV JAVA_HOME /usr/lib/jvm/jre-openjdk/  
  
RUN curl -fsSL get.nextflow.io | bash && chmod 755 nextflow  
RUN mv nextflow /usr/local/bin  
  

