FROM centos:7.2.1511  
COPY CentOS-Base.repo /etc/yum.repos.d/  
RUN yum -y install java-1.7.0-openjdk-headless openssh-server sudo git
openssh-clients sed  
RUN useradd -G wheel -d /jenkins -m jenkins  
RUN echo 'jenkins ALL=(ALL:ALL) NOPASSWD: ALL' >> /etc/sudoers  
RUN mkdir /jenkins/.ssh  
COPY authorized_keys /jenkins/.ssh/  
RUN chown -R jenkins:jenkins /jenkins/.ssh  
RUN chmod 700 /jenkins/.ssh  
RUN chmod 600 /jenkins/.ssh/authorized_keys  
EXPOSE 22  
RUN ssh-keygen -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa  
RUN ssh-keygen -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa  
RUN sed -i 's/Defaults.*requiretty/Defaults !requiretty/' /etc/sudoers

