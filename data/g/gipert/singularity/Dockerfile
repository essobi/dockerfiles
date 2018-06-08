FROM gipert/centos-base:latest  
  
USER root  
  
RUN yum -q install -y squashfs-tools libarchive-devel && \  
yum -q clean all  
  
WORKDIR /tmp  
RUN mkdir -p /tmp/singularity && \  
wget -q -O-
https://github.com/singularityware/singularity/releases/download/2.5.1/singularity-2.5.1.tar.gz
\  
| tar --strip-components 1 -xz -C "/tmp/singularity" && \  
cd /tmp/singularity && \  
./configure && \  
make -j"$(nproc)" && \  
make install && \  
rm -r /tmp/singularity  
  
WORKDIR /data  
CMD /usr/local/bin/singularity  

