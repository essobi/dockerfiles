FROM oraclelinux:6  
RUN yum update -y && \  
curl http://linuxsoft.cern.ch/cern/scl/slc6-scl.repo -o
/etc/yum.repos.d/slc6-scl.repo && \  
sed -i -e 's/gpgcheck=1/gpgcheck=0/g' /etc/yum.repos.d/slc6-scl.repo && \  
yum install tar wget devtoolset-3 -y && \  
yum clean all && \  
rm -r -f /var/cache/yum/*  

