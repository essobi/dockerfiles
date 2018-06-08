# docker build -t jbasney/globus-centos6 .  
# docker run --name globus-centos6 -it jbasney/globus-centos6 /bin/bash  
FROM jbasney/igtf-centos6  
MAINTAINER Jim Basney <jbasney@illinois.edu>  
ENV container docker  
COPY globus-toolkit-repo-latest.noarch.rpm /root  
RUN rpm -hUv /root/globus-toolkit-repo-latest.noarch.rpm && \  
yum -y update && yum -y install \  
gsi-openssh \  
myproxy \  
&& yum clean all  

