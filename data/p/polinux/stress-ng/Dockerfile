FROM centos:7  
LABEL \  
author="Przemyslaw Ozgo" \  
email="linux@ozgo.info" \  
version="0.0.1" \  
description="stress-ng in a docker usefull for stress testing hardware"  
  
ENV SHELL=/bin/bash  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y epel-release && \  
yum install -y libaio libbsd wget && \  
cd /tmp/ && wget
http://dl.fedoraproject.org/pub/fedora/linux/updates/testing/25/x86_64/s/stress-
ng-0.07.05-3.fc25.x86_64.rpm && \  
yum install -y /tmp/stress-ng-0.07.05-3.fc25.x86_64.rpm && \  
rm -f /tmp/stress-ng-0.07.05-3.fc25.x86_64.rpm && \  
yum clean all  
  
ENTRYPOINT ["/usr/bin/stress-ng"]  

