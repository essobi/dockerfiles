#  
# This is a testing image used by origin/test/extended/networking/multicast.go  
#  
# The standard name for this image is openshift/test-multicast  
#  
FROM centos:centos7  
  
RUN INSTALL_PKGS="omping" && \  
yum install -y $INSTALL_PKGS && \  
rpm -V $INSTALL_PKGS && \  
yum clean all  

