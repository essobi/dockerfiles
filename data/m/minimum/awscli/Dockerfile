FROM centos:7  
LABEL maintainer s5550055.minimum@gmail.com  
  
RUN rpm --import https://www.centos.org/keys/RPM-GPG-KEY-CentOS-7 \  
&& yum -y -q install epel-release \  
&& rpm --import http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-7 \  
&& yum -y -q install vim python34 python34-pip jq \  
&& pip3 install -q awscli  
  
ENTRYPOINT ["/usr/bin/aws"]  

