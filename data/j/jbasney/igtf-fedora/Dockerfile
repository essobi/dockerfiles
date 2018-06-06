# docker build -t jbasney/igtf-fedora .  
# docker run --name igtf-fedora -it jbasney/igtf-fedora /bin/bash  
FROM fedora  
MAINTAINER Jim Basney <jbasney@illinois.edu>  
ENV container docker  
COPY igtf.repo /etc/yum.repos.d/igtf.repo  
RUN yum -y update && yum -y install \  
ca_policy_igtf-classic \  
ca_policy_igtf-slcs \  
ca_policy_igtf-mics \  
ca_policy_igtf-iota \  
&& yum clean all  

