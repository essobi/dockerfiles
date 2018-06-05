# docker build --rm -t caso .  
FROM centos:7  
LABEL maintainer "Mario David <mariojmdavid@gmail.com>"  
COPY EGI.repo /etc/yum.repos.d/  
RUN yum -y update && \  
yum -y install epel-release git && \  
yum -y update && \  
yum -y install \  
apel-ssm \  
ca-certificates \  
ca-policy-egi-core \  
ca-policy-lcg \  
python-pip && \  
yum clean all && \  
cd /home && \  
git clone https://github.com/alvarolopez/caso.git -b fix && \  
cd caso && \  
pip install --upgrade pip && \  
pip install . && \  
mkdir -p /etc/caso \  
/etc/apel \  
/var/spool/caso \  
/var/spool/apel/outgoing/openstack \  
/var/log/caso \  
/var/log/apel  
  

