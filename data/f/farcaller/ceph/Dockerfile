FROM ubuntu:14.04  
  
ENV CEPH_VERSION hammer  
  
RUN \  
apt-get update \  
&& apt-get install -y wget unzip \  
&& wget -q -O-
'https://ceph.com/git/?p=ceph.git;a=blob_plain;f=keys/release.asc' | apt-key
add \- \  
&& echo deb http://ceph.com/debian-${CEPH_VERSION}/ trusty main | tee
/etc/apt/sources.list.d/ceph-${CEPH_VERSION}.list \  
&& apt-get update \  
&& apt-get install -y \--force-yes ceph radosgw \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

