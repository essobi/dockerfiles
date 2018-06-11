FROM voidbridge/centos7  
MAINTAINER Voidbridge <developers@voidbridge.com>  
  
RUN curl -Lo /tmp/openshift-origin-client-tools.tar.gz
https://github.com/openshift/origin/releases/download/v1.2.0/openshift-origin-
client-tools-v1.2.0-2e62fab-linux-64bit.tar.gz && \  
tar -zxf /tmp/openshift-origin-client-tools.tar.gz --strip-components 1 -C
/usr/local/bin openshift-origin-client-tools-v1.2.0-2e62fab-linux-64bit/oc  

