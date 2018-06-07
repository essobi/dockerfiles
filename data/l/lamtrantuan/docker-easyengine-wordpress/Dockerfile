## Use official image in master branch  
FROM ubuntu:14.04  
MAINTAINER Lam Tran <lamtt77@gmail.com>  
  
RUN echo "export TERM=xterm" >> /etc/bash.bashrc  
  
## Making EasyEngine aware of our name and email  
COPY ee-gitconfig /root/.gitconfig  
  
RUN echo `cat ~/.gitconfig`  
  
## Get and install EasyEngine  
RUN apt-get install -y wget  
RUN wget -qO ee rt.cx/ee && sudo bash ee  
  
## Source auto completion  
CMD "source /etc/bash_completion.d/ee_auto.rc"  
  
## Wont expose from base image, their extent image will take over  
#EXPOSE 80 443 22222  
# Define default command.  
CMD ["bash"]  

