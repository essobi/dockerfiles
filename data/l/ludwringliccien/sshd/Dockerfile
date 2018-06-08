FROM ubuntu:16.04  
MAINTAINER Ludwring Liccien <ludwring.liccien@gmail.com>  
  
  
RUN apt-get update && apt-get install -y openssh-server git nano  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:screencast' | chpasswd  
  
# Set user deployer  
RUN useradd -g 33 -m deployer && echo "deployer:deployer" | chpasswd &&
adduser deployer sudo  
RUN echo "deployer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
WORKDIR /home/deployer  
  
USER deployer  
  
RUN mkdir .ssh && \  
chmod 700 .ssh && \  
touch .ssh/authorized_keys && \  
chmod 600 .ssh/authorized_keys  
  
COPY authorized_keys /home/deployer/.ssh/authorized_keys  
  
USER root  
  
COPY sshd_config /etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

