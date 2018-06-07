FROM centos:7  
MAINTAINER Danny Ho <danny.ho@hpe.com>  
RUN yum -y install \  
openssh-server \  
epel-release \  
ansible  
RUN yum clean all  
RUN mkdir /var/run/sshd  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN /bin/echo 'root:root'|chpasswd  
RUN /bin/sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional
pam_loginuid.so/g' /etc/pam.d/sshd  
RUN /bin/echo -e "LANG=\"en_US.UTF-8\"" > /etc/default/local  
EXPOSE 22  
CMD /usr/sbin/sshd -D  

