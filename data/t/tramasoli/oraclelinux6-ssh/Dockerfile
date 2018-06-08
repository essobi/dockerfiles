FROM oraclelinux:6  
MAINTAINER Fábio Tramasoli <fabio@tramasoli.com>  
LABEL env=des  
RUN yum -y install openssh-server shadow-utils  
RUN echo "root:hackme" | chpasswd  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

