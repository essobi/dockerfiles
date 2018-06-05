FROM ubuntu:12.04  
MAINTAINER Masahji Stewart <masahji@synctree.com>  
  
RUN apt-get update  
  
RUN apt-get install -y curl  
RUN apt-get install -y less  
RUN apt-get install -y screen  
RUN apt-get install -y sudo  
RUN apt-get install -y vim  
  
RUN adduser deploy  
RUN echo 'deploy ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/deploy-sudo  
RUN chmod 0440 /etc/sudoers.d/deploy-sudo  
  
RUN su - deploy -c "curl -L https://get.rvm.io | bash -s stable"  
RUN su - deploy -c "rvm install ruby-2.1.2"  
  
RUN apt-get install -y git-core  
  
VOLUME /var/log  
  
RUN chown -Rf deploy:deploy /home/deploy  

