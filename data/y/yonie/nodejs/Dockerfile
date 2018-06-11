FROM ubuntu  
  
MAINTAINER yonie (yong_cyril@163.com)  
  
RUN apt-get update  
RUN apt-get install -y xz-utils  
RUN apt-get install -y axel  
  
RUN axel https://nodejs.org/dist/v7.10.0/node-v7.10.0-linux-x64.tar.xz  
  
RUN xz -d *.tar.xz  
RUN tar xvf node-v7.10.0-linux-x64.tar  
RUN cp -rf ./node-v7.10.0-linux-x64/* /usr/local/  
RUN rm -rf node*  
  

