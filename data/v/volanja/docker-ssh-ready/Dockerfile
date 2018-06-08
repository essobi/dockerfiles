FROM centos:centos6  
  
MAINTAINER volanja "https://github.com/volanja/docker_ssh_ready"  
# Packages  
RUN yum update -y  
RUN yum install -y passwd openssh openssh-server openssh-clients initscripts  
  
RUN sed -ri 's/#PermitRootLogin yes/PermitRootLogin yes/g'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
  
RUN service sshd start  
  
EXPOSE 22  
CMD /sbin/init  

