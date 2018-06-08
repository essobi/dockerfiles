FROM centos:7  
MAINTAINER Leon (lvlie) Vliegenthart  
  
# Install packages (needs epel)  
RUN yum install -y epel-release && yum install -y shellinabox openssh-clients
&& yum clean all  
  
# add user for media  
RUN useradd -u 800 ssh  
  
# usuall runs on 8081  
EXPOSE 4200  
# CMD can be easily overwritten for troubleshooting  
CMD /usr/sbin/shellinaboxd -v -t --service "/:ssh:ssh:/home/ssh:/bin/bash"  

