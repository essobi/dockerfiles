FROM tutum/ubuntu:trusty  
  
MAINTAINER Michael Sevilla <mikesevilla3@gmail.com>  
  
RUN apt-get update && apt-get install -y git wget  
  
# install ceph master development branch  
RUN wget -q -O-
'https://ceph.com/git/?p=ceph.git;a=blob_plain;f=keys/autobuild.asc' | sudo
apt-key add - && \  
echo deb http://gitbuilder.ceph.com/ceph-deb-$(lsb_release
-sc)-x86_64-basic/ref/master $(lsb_release -sc) main | sudo tee
/etc/apt/sources.list.d/ceph.list && \  
apt-get update && apt-get install -y --force-yes ceph librados-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# get the code  
RUN mkdir /src && cd /src && \  
git clone \--recursive https://github.com/noahdesu/ceph.git && \  
git clone https://github.com/noahdesu/zlog.git && \  
cd ceph && \  
git checkout -b cls_zlog origin/cls_zlog  
  
# install deps  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && \  
cd /src/ceph && \  
./install-deps.sh && \  
apt-get install -y protobuf-compiler libprotobuf-dev librados2 && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# compile OSD interfaces  
RUN cd /src/ceph && \  
./autogen.sh && \  
./configure && \  
cd src && \  
make libcls_zlog.la && \  
make libcls_zlog_client.la && \  
cp .libs/libcls_zlog.so* /usr/lib/rados-classes/ && \  
cp cls/zlog/cls_zlog_client.h /usr/include/rados/  
  
# compile client interfaces  
RUN cd /src/zlog && \  
autoreconf -ivf && \  
mkdir -p /tmp/install/rados && \  
cp /src/ceph/src/cls/zlog/cls_zlog_client.h /tmp/install/rados && \  
cd /src/zlog && \  
CPPFLAGS=-I/tmp/install LDFLAGS=-L/src/ceph/src/.libs ./configure && \  
cd /src/zlog && \  
make && \  
find /src/zlog/src/ -perm /a+x -exec cp {} /bin/ \;  
  
# Add volumes for Ceph config and data  
VOLUME ["/etc/ceph","/var/lib/ceph"]  
  
# Expose the Ceph ports  
EXPOSE 6789 6800 6801 6802 6803 6804 6805 80 5000 5678  
# Add bootstrap script  
ADD entrypoint.sh /  
RUN chmod 755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

