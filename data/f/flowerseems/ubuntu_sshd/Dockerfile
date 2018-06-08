# sshd on latest ubuntu  
#  
# VERSION 0.0.1  
FROM ubuntu:latest  
MAINTAINER Kenneth Tse  
  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:rootpassword' | chpasswd  
# different ubuntu PermitRootLogin is different, so  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# user is kicked off after login, fix it.  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

