From centos:7  
# Install mongodb  
ADD mongodb-org-3.2.repo /etc/yum.repos.d/  
RUN yum update -y && yum install -y mongodb-org-server mongodb-org-shell && \  
yum clean all  
  
# Add Mongodb custom config  
ADD mongod.conf /etc/mongodb/  
  
EXPOSE 27017  
CMD ["mongod", "-f", "/etc/mongodb/mongod.conf"]

