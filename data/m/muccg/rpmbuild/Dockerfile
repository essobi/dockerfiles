#  
FROM muccg/python-base:centos6-2.7  
MAINTAINER https://github.com/muccg  
  
RUN yum install -y \  
autoconf \  
automake \  
createrepo \  
rpm-build \  
tar \  
yum-utils \  
&& yum clean all  
  
RUN mkdir -p /data/rpmbuild  
  
VOLUME ["/app", "/data"]  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["rpmbuild"]  

