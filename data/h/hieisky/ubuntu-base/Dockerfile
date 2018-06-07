FROM ubuntu:14.04.4  
# Ubuntu 14.04.2 Docker Base with SSH login  
MAINTAINER Hisiky Ma <hieiskyapp@gmail.com>  
  
USER root  
  
# apt-get update & upgrade  
RUN apt-get update -y  
  
# Install commonly used package  
RUN apt-get install -y sudo unzip wget net-tools vim.tiny ca-certificates  
  
# Install sshd  
RUN apt-get install -y openssh-server;  
RUN mkdir /var/run/sshd  
RUN echo 'root:admin' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Clean up the  
RUN apt-get clean  
RUN apt-get autoremove -y  
  
# Expose ports  
EXPOSE 22  
CMD ["bash"]  

