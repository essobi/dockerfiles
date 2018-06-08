FROM centos  
  
MAINTAINER scanales  
  
RUN yum install -y openssh-server sudo  
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
  
RUN yum install -y openssh-clients  
  
RUN yum install -y unzip  
RUN yum install -y rsync  
  
RUN echo "root:root" | chpasswd  
RUN echo "root ALL=(ALL) ALL" >> /etc/sudoers  
  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
  
RUN mkdir /var/run/sshd  
  
EXPOSE 22  
EXPOSE 4713  
EXPOSE 4712  
EXPOSE 23364  
EXPOSE 9993  
EXPOSE 9990  
EXPOSE 54200  
EXPOSE 55200  
EXPOSE 45688  
EXPOSE 57600  
EXPOSE 7600  
EXPOSE 45700  
EXPOSE 3529  
EXPOSE 8443  
EXPOSE 8080  
EXPOSE 8009  
EXPOSE 9999  
CMD ["/usr/sbin/sshd", "-D"]  

