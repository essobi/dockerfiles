FROM centos:7  
MAINTAINER Fábio Tramasoli <fabio@tramasoli.com>  
LABEL env=dev  
RUN yum -y install openssh-server shadow-utils && yum clean all  
COPY ./scripts/Dockerfile-ssh.bootstrap /bootstrap.sh  
EXPOSE 22  
CMD ["/bin/bash","/bootstrap.sh"]  

