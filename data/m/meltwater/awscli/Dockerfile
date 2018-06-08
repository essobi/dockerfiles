FROM centos:6  
# Install Fedora EPEL YUM repo  
RUN rpm -i "https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm"  
  
# Install the PIP Python package manager  
RUN yum -y install python-pip && yum clean all  
  
# Install AWS Command Line Interface  
RUN pip install awscli  
  
COPY launch.sh /  
ENTRYPOINT ["/launch.sh"]  

