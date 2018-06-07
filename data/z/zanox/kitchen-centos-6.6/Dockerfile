FROM centos:6.6  
RUN yum update -y  
RUN yum install -y yum-plugin-ovl  
RUN rpm --rebuilddb && yum clean all  
RUN yum install -y net-tools  
RUN yum install -y curl sudo openssh-server cron vim netcat-traditional  
  
RUN echo 'Defaults !requiretty' >> /etc/sudoers  
# Chef version on nodes is 11.4.0, but we need 12.5+ to handle some bugs with
knife + berkshelf + test kitchen - see SE-1347  
RUN curl -L https://www.opscode.com/chef/install.sh | sudo bash -s -- -v
12.6.0  

