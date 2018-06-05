FROM fedora:25  
MAINTAINER Sergio M.V. <smveloso@gmail.com>  
  
LABEL description="bbwarsaw"  
  
ADD
https://www14.bancobrasil.com.br/downloads/ws/linux/diagbb-1.0.fedora25.x86_64.rpm
/opt  
#Alternatively, if you have a local copy ...  
#ADD diagbb-1.0.fedora25.x86_64.rpm /opt  
# Installs required dependencies, the warsaw package itself and then cleans
everything up  
RUN dnf makecache && \  
dnf -y install openssl-1:1.0.2k-1.fc25 redhat-lsb-4.1-33.fc25 && \  
rpm -ivh /opt/diagbb-1.0.fedora25.x86_64.rpm && \  
dnf clean all && \  
rm -rf /var/cache/dnf/* && \  
rm -f /opt/diagbb-1.0.fedora25.x86_64.rpm  
  
# For now ...  
CMD ["/bin/bash"]  

