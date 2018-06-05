FROM starlabio/centos-native-build:1.0  
MAINTAINER Jonathan Creekmore <jonathan@starlab.io>  
  
# dracut depends  
RUN yum install dracut-network nfs-utils -y && \  
yum clean all && \  
rm -rf /var/cache/yum/* /tmp/* /var/tmp/*  
  
COPY dracut.conf /etc/dracut.conf  
  
VOLUME ["/source"]  
WORKDIR /source  
CMD ["/bin/bash"]  

