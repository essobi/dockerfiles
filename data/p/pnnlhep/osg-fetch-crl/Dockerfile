FROM centos:centos7  
MAINTAINER Kevin Fox "Kevin.Fox@pnnl.gov"  
ADD ./start.sh /etc/start.sh  
RUN \  
yum install -y epel-release; \  
yum install -y http://repo.grid.iu.edu/osg/3.4/osg-3.4-el7-release-latest.rpm;
\  
yum clean all; \  
yum install -y fetch-crl osg-ca-certs perl-Crypt-SSLeay rsync && \  
mv /etc/grid-security/certificates /etc/grid-security/certificates.orig && \  
chmod +x /etc/start.sh  
  
CMD ["/etc/start.sh"]  

