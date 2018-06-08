FROM skarllot/centos:6.5  
MAINTAINER skarllot@gmail.com  
  
# Adds required packages  
RUN yum --releasever=6.5 -y install git fuse && \  
yum clean all --releasever=6.5  
  
# Install Cloudfuse  
RUN yum --releasever=6.5 -y install gcc make fuse-devel curl-devel \  
libxml2-devel openssl-devel && \  
yum clean all --releasever=6.5  
RUN cd /usr/local && git clone https://github.com/redbo/cloudfuse.git  
RUN cd /usr/local/cloudfuse && git checkout
21358f159d13c6196cee17652fd3d415dfd984f3  
RUN cd /usr/local/cloudfuse && ./configure && make && make install  
RUN yum --releasever=6.5 -y remove \\*-devel && \  
yum clean all --releasever=6.5  
RUN mkdir /var/cloudfuse  
  
ADD assets/ /root/config/  
  
ENTRYPOINT ["/root/config/init"]  
CMD ["start"]  

