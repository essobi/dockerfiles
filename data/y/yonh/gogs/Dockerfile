# Version 0.0.1  
# build  
# sudo docker build -t yonh/gogs3 .  
# run  
# sudo docker run -d -p 2222:22 -p 3000:3000 --name gogs yonh/gogs  
# sudo docker run -d -p 2222:22 -p 3000:3000 --name gogs -v
/var/gogs:/home/git yonh/gogs  
# basic image  
FROM ubuntu:14.04  
MAINTAINER yonh "azssjli@163.com"  
ENV REFERSHED_AT 2016-03-05  
RUN apt-get update  
RUN apt-get install -y git openssh-server && rm -rf /var/lib/apt/lists/*  
  
run adduser git  
add gogs /opt/gogs  
run chown git:git /home/git -R  
# modify default ssh port  
#add sshd_config /etc/ssh/sshd_config  
RUN mkdir /var/run/sshd  
  
add run.sh /run.sh  
run chmod 777 /run.sh  
  
EXPOSE 22 3000  
CMD ["/run.sh"]  

