FROM centos:7.3.1611  
CMD mkdir -p /root/vagrant  
WORKDIR /root/vagrant  
RUN yum -y install epel-release && \  
yum -y install ansible && \  
yum -y install openssh && \  
yum -y clean all  
RUN curl -Os
https://releases.hashicorp.com/vagrant/1.9.6/vagrant_1.9.6_x86_64.rpm  
RUN yum install -y vagrant_1.9.6_x86_64.rpm && \  
vagrant plugin install vagrant-openstack-provider && \  
rm vagrant_1.9.6_x86_64.rpm  
CMD ["/bin/bash","/usr/bin/vagrant","up"]  

