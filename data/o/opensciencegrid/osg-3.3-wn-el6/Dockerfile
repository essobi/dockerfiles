FROM centos:centos6  
  
RUN yum -y install http://repo.grid.iu.edu/osg/3.3/osg-3.3-el6-release-
latest.rpm && \  
yum -y install epel-release \  
yum-plugin-priorities && \  
yum -y install osg-wn-client \  
osg-wn-client-glexec \  
redhat-lsb-core  
  
# Install Singularity  
RUN yum -y install \--enablerepo osg-upcoming-development singularity && \  
yum clean all  

