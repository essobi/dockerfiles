FROM centos:7  
MAINTAINER kanga333  
  
RUN yum clean all && \  
yum update -y && \  
yum install -y unzip which && \  
yum clean all  
  
ENV ENTRYKIT_VERSION="0.4.0"  
RUN curl -L -o /tmp/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz \  
https://github.com/progrium/entrykit/releases/download/v${ENTRYKIT_VERSION}/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz
&& \  
tar xvfz /tmp/entrykit_${ENTRYKIT_VERSION}_Linux_x86_64.tgz -C /tmp/ && \  
mv /tmp/entrykit /bin/ && \  
entrykit --symlink && \  
rm -rf /tmp/entrykit*  
  
ENTRYPOINT ["/bin/bash"]  

