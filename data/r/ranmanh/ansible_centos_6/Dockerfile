FROM centos:6  
RUN yum -y install epel-release  
RUN yum -y update  
RUN yum -y install python-pip ansible  
RUN pip install --upgrade pip  
  
# Clean Up  
RUN yum clean all  
  
CMD ["/sbin/init"]  

