###################################################################  
## ##  
## Docker file of Docker image with NodeJS for WARP projects ##  
## ##  
###################################################################  
## Table of contents  
##  
## 1. Base image and developers  
## 2. Suppress messages error/warning from upstart  
## 3. Let the container know about the absence of tty  
## 4. Erase of script file /usr/sbin/policy-rc.d  
## 5. Update packages info, install additional  
## 6. Install bower and gulp globally  
## 7. Intall all neccesary packages  
## 8. Create supervisor catalogue, if it is absent  
## 9. Set default cmd for supervisord  
## 10. Configure SSH daemon  
##  
# 1. Base image and developers  
FROM node:latest  
MAINTAINER German Manvelov <gtmmm2011@gmail.com>  
  
# 2. Suppress messages error/warning from upstart  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
  
# 3. Let the container know about the absence of tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# 4. Erase of script file /usr/sbin/policy-rc.d  
# - It'll allow to avoid the error: "invoke-rc.d: policy-rc.d denied execution
of start"  
# - More details see here: https://habrahabr.ru/post/247903/  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
  
# 5. Update packages info, install additional  
RUN apt-get update && apt-get -y upgrade && apt-get install -y \  
  
openssh-server  
  
# 6. Install bower and gulp globally  
RUN npm install -g gulpjs/gulp#4.0  
RUN npm install -g bower  
  
# 7. Intall all necessary packages  
RUN apt-get update && apt-get install -y \  
  
curl \  
cron \  
supervisor  
  
# 8. Create supervisor catalogue, if it is absent  
RUN mkdir -p /var/log/supervisor  
  
# 9. Set default cmd for supervisord  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor.d/supervisor-docker-node-
dev.ini"]  
  
# 10. Configure SSH daemon  
# 10.1. Set admin password  
RUN echo 'root:password' | chpasswd  
  
# 10.2. Allow root-login without password via SSH to container within inner
network  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# 10.3. SSH login fix. Otherwise user is kicked off after loginи  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  

