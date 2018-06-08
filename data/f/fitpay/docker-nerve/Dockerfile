FROM centos:7  
MAINTAINER Scott Stevelinck <scott@fit-pay.com>  
  
RUN yum update -y && yum clean all  
  
RUN yum install -y gem make gcc patch ruby-devel && yum clean all  
RUN gem install nerve  
  
ADD /run.sh /run.sh  
RUN chmod 755 /run.sh  
  
ENTRYPOINT ["/run.sh"]  
CMD ["run"]  

