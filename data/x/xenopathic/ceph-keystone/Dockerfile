# DOCKER-VERSION 1.0.0  
#  
# Automated Ceph full-stack environment  
# Inspired by ceph/demo  
#  
# VERSION 0.0.1  
FROM ceph/base  
MAINTAINER Robin McCorkell "robin@mccorkell.me.uk"  
RUN apt-get update && apt-get install -y --force-yes keystone && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

