FROM qnib/ceph-base  
  
RUN apt-get install -y --force-yes ceph radosgw && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install etcdctl  
RUN wget -q -O-
"https://github.com/coreos/etcd/releases/download/${ETCDCTL_VERSION}/etcd-${ETCDCTL_VERSION}-${ETCDCTL_ARCH}.tar.gz"
|tar xfz - -C/tmp/ etcd-${ETCDCTL_VERSION}-${ETCDCTL_ARCH}/etcdctl  
RUN mv /tmp/etcd-${ETCDCTL_VERSION}-${ETCDCTL_ARCH}/etcdctl
/usr/local/bin/etcdctl  
  
#install kviator  
RUN curl -fsL
https://github.com/AcalephStorage/kviator/releases/download/v${KVIATOR_VERSION}/kviator-${KVIATOR_VERSION}-linux-
amd64.zip |bsdtar xf - -C /usr/local/bin/ && \  
chmod +x /usr/local/bin/kviator  
  
# Install confd  
RUN curl -fso /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 && \  
chmod +x /usr/local/bin/confd && \  
mkdir -p /etc/confd/conf.d \  
/etc/confd/templates  
  
RUN pip install envoy  
ADD opt/qnib/ceph/bin/start.sh /opt/qnib/ceph/bin/  
ADD etc/supervisord.d/ceph.ini /etc/supervisord.d/  
ADD opt/qnib/ceph/mon/bin/isok.sh /opt/qnib/ceph/mon/bin/  
ADD opt/qnib/ceph/mds/bin/isok.sh /opt/qnib/ceph/mds/bin/  
ADD opt/qnib/ceph/osd/bin/isok.sh /opt/qnib/ceph/osd/bin/  
ADD opt/qnib/ceph/radosgw/bin/isok.sh /opt/qnib/ceph/radosgw/bin/  
ADD etc/consul.d/*.json /etc/consul.d/  
ADD etc/supervisord.d/rados-add-user.ini /etc/supervisord.d/  
ADD opt/qnib/ceph/bin/create_rados_user.py /opt/qnib/ceph/bin/  
  
VOLUME ["/var/lib/ceph/"]  

