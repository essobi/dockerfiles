FROM centos:7  
LABEL name="OSG 3.4 OSG-Build client"  
  
RUN yum -y install
https://repo.opensciencegrid.org/osg/3.4/osg-3.4-el7-release-latest.rpm && \  
yum -y install epel-release \  
yum-plugin-priorities && \  
yum -y install --enablerepo=osg-development \  
globus-proxy-utils \  
redhat-lsb-core \  
osg-build && \  
yum clean all --enablerepo=\\* && \  
rm -rf /var/cache/yum/*  
  
RUN groupadd u && \  
useradd -g u -G mock -m -d /u u && \  
install -d -o u -g u -m 0755 /u/.osg-koji && \  
ln -s /u/.osg-koji /u/.koji && \  
chown u:u /u/.koji  
  
COPY input/osg-ca-bundle.crt /u/.osg-koji/osg-ca-bundle.crt  
COPY input/config /u/.osg-koji/config  
COPY input/command-wrapper.sh /usr/local/bin/command-wrapper.sh  
  
USER u  
WORKDIR /u  

