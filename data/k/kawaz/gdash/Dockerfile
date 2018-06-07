FROM centos:7  
MAINTAINER Yoshiaki Kawazu kawazzz@gmail.com  
  
RUN \  
curl -sL -o /etc/yum.repos.d/glusterfs-epel.repo
http://download.gluster.org/pub/gluster/glusterfs/LATEST/EPEL.repo/glusterfs-
epel.repo && \  
yum install -y --enablerepo=glusterfs-epel glusterfs-\\* && \  
yum install -y http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm && \  
yum install -y python-pip && \  
pip install gdash && \  
yum clean all  
  
EXPOSE 8080  
ENTRYPOINT gdash  

