FROM corfr/ceph-base  
  
RUN ( \  
apt-get update && \  
apt-get upgrade -y && \  
ln -sf /bin/bash /bin/sh \  
)  
  
RUN ( \  
apt-get update && \  
apt-get --yes --assume-yes install -y python-software-properties software-
properties-common wget \  
)  
  
RUN ( \  
add-apt-repository ppa:saltstack/salt && \  
apt-get update \  
)  
  
RUN ( \  
apt-get install -y salt-minion \  
)  
  
ENV BASE_URL http://cor-net.org/wp-content/uploads/2015/02/calamari-
repo/precise/pool/main/d/diamond  
ENV BASE_DIAMOND_FILE diamond_3.4.67_all.deb  
  
RUN ( \  
wget --quiet ${BASE_URL}/${BASE_DIAMOND_FILE} && \  
( dpkg -i ${BASE_DIAMOND_FILE} || true ) && \  
apt-get --yes --assume-yes install -f && \  
rm ${BASE_DIAMOND_FILE} \  
)  
  
ADD entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  

