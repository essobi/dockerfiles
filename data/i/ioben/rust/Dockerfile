FROM centos:7  
MAINTAINER Ben "ben@ros.io"  
ENV USER root  
  
RUN yum install -y gcc file && yum clean all  
RUN echo '#!/bin/bash' > /usr/bin/sudo && \  
echo 'exec $@' >> /usr/bin/sudo && \  
chmod +x /usr/bin/sudo; \  
curl -sSf https://static.rust-lang.org/rustup.sh | sh; \  
rm /usr/bin/sudo  
  

