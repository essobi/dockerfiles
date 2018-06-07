FROM node:5-slim  
  
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
# config package.json file url  
ENV PACKAGE_GIT_URL=https://raw.githubusercontent.com/FayeHuang/react-
template/master/package.json  
  
WORKDIR /usr/src/app  
RUN wget $PACKAGE_GIT_URL -O ../package.json  
RUN npm install --prefix=../  
COPY webpack-dev-server_start.sh /etc/init.d/webpack-dev-server_start.sh  
  
COPY supervisord.conf /etc/supervisord.conf  
EXPOSE 22 8888  
CMD ["/usr/local/bin/supervisord", "-c", "/etc/supervisord.conf"]  

