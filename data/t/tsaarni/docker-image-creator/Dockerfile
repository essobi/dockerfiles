FROM centos:6  
MAINTAINER tero.saarni@gmail.com  
  
# EPEL repository needed for python-imgcreate  
RUN yum install -y epel-release  
  
RUN yum install -y python-imgcreate git tar gzip  
  
RUN git clone https://github.com/katzj/ami-creator.git /usr/local/ami-creator  
  
ADD docker-image-creator-helper /usr/bin/  
  
ENTRYPOINT ["/usr/bin/docker-image-creator-helper"]  

