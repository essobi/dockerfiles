FROM node:7.8.0  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:docker' | chpasswd  
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN npm install -g ionic cordova  
  
WORKDIR /home  
  
RUN git clone https://github.com/gnflow/ionic-gf-app  
WORKDIR /home/ionic-gf-app  
RUN npm install  
  
EXPOSE 80 8888 35729 22  

