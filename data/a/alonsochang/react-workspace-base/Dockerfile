FROM node:7.7.4-slim  
  
RUN apt-get update -y && apt-get install sudo vim openssh-server git python-
pip -y && apt-get clean all  
RUN pip install supervisor  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:changeme' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
# set root ssh login workdir  
RUN echo 'cd /usr/src/app' >> /root/.bash_profile  
  
# == begin to set react workspace ==  
RUN npm install -g n  
RUN n 8.11.2  
  
EXPOSE 22 8888  

