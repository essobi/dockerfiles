FROM mattdm/fedora  
MAINTAINER Praveen Kumar "kumarpraveen.nitdgp@gmail.com"  
RUN yum -y update  
RUN yum -y install openssh-server  
RUN yum -y install supervisor  
  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/run/supervisord  
RUN echo "root:password" | chpasswd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
RUN sed -i 's|session required pam_loginuid.so|session optional
pam_loginuid.so|g' /etc/pam.d/sshd  
  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22  
ENTRYPOINT ["/usr/bin/supervisord", "-n"]  

