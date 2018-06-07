FROM centos  
MAINTAINER Shaun Martin <shaun@samsite.ca>  
  
EXPOSE 137/udp 138/udp 139 445  
ENV SHARENAMES # sharenames should be a space separated list  
ENV USER # default: samba  
ENV PASSWORD # in the clear! hurray! default: password  
ENV WORKGROUP # default: WORKGROUP  
RUN rpm -ivh http://yum.puppetlabs.com/puppetlabs-release-el-7.noarch.rpm  
RUN yum install -y puppet  
RUN yum install -y tar  
RUN yum install -y hostname  
RUN puppet module install ajjahn/samba  
RUN puppet module install saz/sudo  
RUN puppet module install ajcrowe-supervisord  
  
ADD launch.sh /launch.sh  
RUN chmod +x /launch.sh  
  
ENTRYPOINT /bin/bash /launch.sh  

