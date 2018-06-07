FROM debian:stretch-slim  
  
ADD https://github.com/openshift/origin/releases/download/v3.6.0/openshift-
origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz /tmp/  
RUN cd /tmp/ && tar xvf openshift-*  
RUN mv /tmp/openshift-*/oc /usr/local/bin/ && chmod 755 /usr/local/bin/oc  

