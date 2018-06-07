FROM debian:jessie  
  
LABEL maintainer="Hiroki Danno <redgrapefruit@mac.com>" \  
description="A containerized Drop-seq Tools" \  
license="MIT"  
  
ENV PATH=/usr/local/Drop-seq_tools-1.0:$PATH  
  
# install Drop-seq_tools-*  
RUN echo "deb http://http.debian.net/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get update && \  
apt-get install --yes \  
-t jessie-backports \  
openjdk-8-jre-headless \  
unzip \  
wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/ && \  
ZIP=Drop-seq_tools-1.11.zip && \  
wget http://mccarrolllab.com/wp-content/uploads/2015/05/$ZIP -O /tmp/$ZIP && \  
unzip /tmp/$ZIP -d /usr/local && \  
chmod -R 755 /usr/local/Drop-seq_tools-1.0 && \  
rm /tmp/$ZIP  
  
CMD ["/bin/bash"]  

