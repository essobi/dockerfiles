FROM centos:centos7  
  
# Install the basic requirements  
RUN yum -y install epel-release && yum -y update && yum -y install nss_wrapper
gettext && yum clean all  
  
RUN mkdir -p /usr/local/share  
COPY passwd.template /usr/local/share/passwd.template  
COPY init.sh /usr/local/bin/init.sh  
  
CMD ["/usr/local/bin/init.sh"]  
  
# Local Variables:  
# docker-image-name: "syndesis/nsswrapper:latest"  
# End:  

