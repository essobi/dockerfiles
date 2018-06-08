FROM centos:7  
MAINTAINER garethahealy (https://github.com/garethahealy/)  
  
LABEL Name="centos-pod-pause" \  
Vendor="com.garethahealy" \  
Version="1.0.0" \  
License="Apache License, Version 2.0"  
  
USER root  
  
ADD pause.c /pause-code/pause.c  
  
# Compiler tools  
RUN yum install -y gcc kernel-devel make && \  
yum clean all  
  
# Compile pause  
RUN cd /pause-code && \  
cc -o pause pause.c  
  
ENTRYPOINT ["/pause-code/pause"]  

