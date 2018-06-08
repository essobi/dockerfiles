# docker build -t jbasney/globus .  
# docker run --name globus -it jbasney/globus /bin/bash  
FROM jbasney/igtf-centos  
MAINTAINER Jim Basney <jbasney@illinois.edu>  
ENV container docker  
COPY globus-toolkit-repo-latest.noarch.rpm /root  
RUN rpm -hUv /root/globus-toolkit-repo-latest.noarch.rpm && \  
yum -y update && yum -y install \  
gsi-openssh-clients \  
myproxy \  
perl-Crypt-SSLeay perl-LWP-Protocol-https perl-Mozilla-CA perl-Term-UI \  
&& yum clean all  

