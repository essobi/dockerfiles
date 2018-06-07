FROM centos:7  
RUN yum install -y \  
filebench \  
&& \  
yum clean all  
  
COPY runner.sh /  
RUN chmod 755 /runner.sh  
  
#-- Run as non-root  
RUN useradd -M filebench  
USER filebench:filebench  
  
ENTRYPOINT ["/runner.sh"]  

