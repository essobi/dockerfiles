FROM centos:6  
MAINTAINER Sam Song <samsong8610@gmail.com>  
  
RUN yum clean all && yum update -y  
RUN yum install -y epel-release  
RUN yum install -y git \  
python-virtualenv python-pip  
  
RUN mkdir /src  
  
VOLUME /data  
  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
CMD ["/start.sh"]  

