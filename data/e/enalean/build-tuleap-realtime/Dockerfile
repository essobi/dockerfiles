FROM centos:6  
  
RUN yum install -y epel-release && \  
yum install -y nodejs npm jq tar nodejs-packaging rpm-build && \  
yum clean all && \  
npm config \--global set cafile /etc/pki/tls/certs/ca-bundle.crt && \  
npm config \--global set ca null  
  
VOLUME /realtime  
  
CMD make -C /realtime/packaging build  

