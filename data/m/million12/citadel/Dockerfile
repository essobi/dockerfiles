FROM million12/ssh  
MAINTAINER Przemyslaw Ozgo <linux@ozgo.info>  
  
ENV DOMAIN=example.org \  
PASSWORD=default-password \  
ATOM_SUPPORT=false  
  
RUN \  
cd /etc/yum.repos.d/ && \  
wget
http://download.opensuse.org/repositories/home:homueller:citadel/CentOS_7/home:homueller:citadel.repo
&& \  
rpm --rebuilddb && yum clean all && \  
yum install -y deltarpm && \  
yum install -y bind citadel webcit && \  
yum clean all  
  
ADD container-files/ /  
  
EXPOSE 25 110 143 465 587 993 995 8080  

