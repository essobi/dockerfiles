FROM erickagrazal/baseline-centos  
MAINTAINER Erick Agrazal "erick.agrazal@gmail.com"  
# Installation:  
# Import MongoDB public GPG key AND create a MongoDB list file  
RUN echo -e "[mongodb]\nname=MongoDB Repository\nbaseurl=http://downloads-
distro.mongodb.org/repo/redhat/os/`uname -m`/\ngpgcheck=0\nenabled=1" >
/etc/yum.repos.d/mongodb.repo  
  
# Update yum sources, clean AND install MongoDB  
RUN yum -y update  
RUN yum install -y mongodb-org  
RUN yum clean all  
  
# Create the MongoDB data directory  
RUN mkdir -p /data/db  
  
# Create Volumes to expose the folder to the outside  
VOLUME ["/data/db"]  
WORKDIR /data  
  
# Expose port 27017 from the container to the host  
EXPOSE 27017  
# Set usr/bin/mongod as the dockerized entry-point application  
ENTRYPOINT ["/usr/bin/mongod"]  

