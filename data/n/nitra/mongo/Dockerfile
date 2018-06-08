# Dockerizing MongoDB: Dockerfile for building MongoDB images  
FROM nitra/centos7  
MAINTAINER Nitra  
#Install MONGO3 and configure  
#RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
RUN yum clean all && yum -y update  
RUN yum install -y ntp mc psmisc initscripts rootfiles file glibc-common  
ADD mongodb.repo /etc/yum.repos.d/mongodb.repo  
RUN yum install -y mongodb-org numactl  
ADD mongod.conf /etc/mongod.conf  
RUN chmod 644 /etc/mongod.conf  
ADD start.sh /start.sh  
ADD mongo_restart /mongo_restart  
RUN chmod +x /start.sh /mongo_restart  
RUN ln -s /mongo_restart.sh /usr/bin/mongo_restart  
#Install locale  
RUN rm -rf /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Kiev /etc/localtime  
RUN sed -i "s/4096/32000/" /etc/security/limits.d/20-nproc.conf  
# Expose port #27017 from the container to the host  
EXPOSE 27017  
CMD ["/start.sh"]  

