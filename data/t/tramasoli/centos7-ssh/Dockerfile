FROM centos:7  
MAINTAINER Fábio Tramasoli <fabio@tramasoli.com>  
LABEL env=des  
RUN yum -y install openssh-server shadow-utils  
COPY ./scripts/bootstrap.sh /bootstrap.sh  
EXPOSE 22  
CMD ["/bin/bash","/bootstrap.sh"]  

