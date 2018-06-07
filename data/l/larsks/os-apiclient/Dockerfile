FROM fedora:20  
MAINTAINER Lars Kellogg-Stedman <lars@oddbit.com>  
  
RUN yum -y install python-keystoneclient  
RUN yum -y install python-glanceclient  
RUN yum -y install python-novaclient  
  
ADD keystonerc /root/keystonerc  
ADD setup-keystone.sh /root/setup-keystone.sh  
ADD setup-glance.sh /root/setup-glance.sh  
ADD setup-nova.sh /root/setup-nova.sh  
ADD add-keystone-service.sh /root/add-keystone-service.sh  
  
RUN echo '. $HOME/keystonerc' >> /root/.bash_profile  
  
CMD su - root  
  

