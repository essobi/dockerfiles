FROM centos:centos7  
MAINTAINER Charles Drolet-Achkar <charles.drokar@gmail.com>  
  
# Update the image  
RUN yum update -y  
  
# Add s6 overlay v1.14.0.3 (https://github.com/just-containers/s6-overlay)  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v1.14.0.3/s6-overlay-amd64.tar.gz
/tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C /  
  
ENTRYPOINT ["/init"]  

