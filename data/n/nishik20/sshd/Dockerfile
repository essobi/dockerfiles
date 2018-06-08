FROM centos:6  
RUN yum update -y  
RUN yum install -y passwd  
RUN yum install -y openssh  
RUN yum install -y openssh-server  
RUN yum install -y openssh-clients  
RUN yum install -y sudo  
  
# sshd setup  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config  
RUN /sbin/service sshd start  
RUN /sbin/service sshd stop  
  
# user setup  
RUN echo 'root:docker' | chpasswd  
RUN useradd docker  
RUN echo 'docker:docker' | chpasswd  
RUN echo "docker ALL=(ALL) ALL" >> /etc/sudoers.d/docker  
RUN chmod 644 /etc/sudoers.d/docker  
  
# sshd start  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

