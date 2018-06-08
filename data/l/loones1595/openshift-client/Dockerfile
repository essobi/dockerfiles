FROM centos:7  
MAINTAINER Alex Eng <loones1595@gmail.com>  
ENV OC_VERSION "v3.6.0-alpha.2"  
ENV OC_RELEASE "openshift-origin-client-
tools-v3.6.0-alpha.2-3c221d5-linux-64bit.tar.gz"  
# install the oc client tools  
ADD
https://github.com/openshift/origin/releases/download/$OC_VERSION/$OC_RELEASE
/opt/oc/release.tar.gz  
RUN tar --strip-components=1 -xzvf /opt/oc/release.tar.gz -C /opt/oc/ && \  
mv /opt/oc/oc /usr/bin/ && \  
rm -rf /opt/oc  
  
EXPOSE 8001  
CMD /usr/bin/oc  

