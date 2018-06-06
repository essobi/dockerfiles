FROM gbraad/openstack-client:ubuntu  
MAINTAINER Giorgio Regni <gr@scalilty.com>  
  
# Some developement tools you may want to have at your disposal  
RUN apt-get update  
RUN apt-get install -y python-pip libxml2-dev libxmlsec1-dev  
RUN pip install python-saml  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME ["/root/.stack", "/root/.config/openstack", "/workspace"]  
WORKDIR /workspace  
  
CMD ["bash"]  
  

