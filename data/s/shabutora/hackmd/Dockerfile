FROM node:0.12.7  
MAINTAINER Tsukasa Tamaru<tsukasa@iyher.net>  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y git  
RUN npm install -g pm2  
  
RUN git clone https://github.com/shabutora/hackmd.git /opt/hackmd  
  
WORKDIR /opt/hackmd  
  
RUN npm install  
  
EXPOSE 80  
EXPOSE 443  
CMD pm2 start processes.json && tail -f logs/hackmd_out.log  
  

