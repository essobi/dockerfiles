FROM ivotron/cephdev  
  
MAINTAINER Ivo Jimenez "ivo.jimenez@gmail.com"  
  
## what follows is a simplified version of ceph/base's Dockerfile  
  
RUN apt-get update && apt-get install -y wget unzip && \  
wget -q -O- 'https://ceph.com/git/?p=ceph.git;a=blob_plain;f=keys/release.asc'
| apt-key add - && \  
echo deb http://ceph.com/debian-hammer/ trusty main | tee
/etc/apt/sources.list.d/ceph-hammer.list && \  
apt-get install -y --force-yes \  
ceph \  
ceph-dbg \  
ceph-mds \  
ceph-mds-dbg \  
ceph-common \  
ceph-common-dbg \  
ceph-fuse \  
ceph-fuse-dbg \  
ceph-test \  
ceph-test-dbg \  
radosgw \  
radosgw-dbg \  
python-ceph \  
libcephfs1 \  
libcephfs1-dbg \  
librados2 \  
librados2-dbg \  
librbd1 \  
librbd1-dbg \  
rbd-fuse && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir /ceph  

