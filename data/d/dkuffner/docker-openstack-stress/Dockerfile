FROM centos  
ENTRYPOINT ["/start"]  
  
# Arguments for start process.  
ENV ARGS --help  
ADD start /start  
RUN chmod +x /start  
  
# Install epel.  
RUN rpm -ivh http://mirror.de.leaseweb.net/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
# Install stress.  
RUN yum install -y stress  
  
# Cloud init.  
RUN mkdir -p /etc/cloud  
ADD cloud.cfg /etc/cloud/cloud.cfg  
RUN yum install -y cloud-init  

