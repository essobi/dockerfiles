FROM ubuntu:16.04  
# Install any needed packages specified in requirements.txt  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get -y install openssl file sudo net-tools inetutils-ping dnsutils vim
curl openssh-server  
  
RUN mkdir /var/run/sshd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN mkdir /root/.ssh  
ADD entrypoint.sh /root/entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/root/entrypoint.sh"]  
  

