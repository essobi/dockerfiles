FROM centos:centos7  
  
RUN yum install -y wget && \  
yum clean all && \  
pushd /tmp && \  
wget https://github.com/openshift/origin/releases/download/v3.6.0/openshift-
origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz && \  
tar -xvzf openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit.tar.gz && \  
cp openshift-origin-client-tools-v3.6.0-c4dd4cf-linux-64bit/oc /usr/bin && \  
chmod +x /usr/bin/oc && rm -rf /tmp/openshift* && \  
popd  
  
ENTRYPOINT ["/usr/bin/oc", "proxy"]

