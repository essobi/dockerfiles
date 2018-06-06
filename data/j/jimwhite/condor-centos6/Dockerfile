FROM centos:centos6  
MAINTAINER Jim White <mailto:jimwhite@uw.edu>  
  
# Here I only install tools which we must have:  
RUN yum -y install yum-utils wget which && \  
wget http://research.cs.wisc.edu/htcondor/yum/RPM-GPG-KEY-HTCondor && \  
rpm --import RPM-GPG-KEY-HTCondor && \  
yum-config-manager --add-repo
https://research.cs.wisc.edu/htcondor/yum/repo.d/htcondor-stable-rhel6.repo &&
\  
yum -y install condor.x86_64 condor-debuginfo condor-python && \  
yum clean all  
  
CMD [ "/bin/bash" ]  

