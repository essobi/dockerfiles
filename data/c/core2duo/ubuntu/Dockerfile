FROM ubuntu:14.04  
MAINTAINER Alex King "core2duoe6420@gmail.com"  
  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak  
  
RUN echo "deb http://mirrors.163.com/ubuntu/ trusty main restricted universe
multiverse\n\  
deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe
multiverse\n\  
deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe
multiverse\n\  
deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe
multiverse\n\  
deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe
multiverse\n\  
deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe
multiverse\n\  
deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted
universe multiverse\n\  
deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe
multiverse\n\  
deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted
universe multiverse\n\  
deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted
universe multiverse\n\  
" > /etc/apt/sources.list  
  
CMD [ "/bin/bash" ]  

