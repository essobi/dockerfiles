FROM ubuntu:trusty  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.orig  
#RUN sed 's/arch/cn\\.arch/' /etc/apt/sources.list.orig >
/etc/apt/sources.list  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install openssh-server  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:MustChange' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
RUN touch /initrc  
RUN echo "/usr/bin/service ssh start" >> /initrc  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
EXPOSE 22  
CMD ["/bin/bash", "--rcfile", "/initrc"]  

