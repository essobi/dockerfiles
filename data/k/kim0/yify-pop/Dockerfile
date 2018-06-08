FROM ubuntu:14.04  
MAINTAINER Ahmed Kamal <email.ahmedkamal@googlemail.com>  
  
RUN apt-get update && apt-get install nodejs npm git nodejs-legacy -qy  
RUN npm -g install geddy peerflix  
RUN git clone https://github.com/yify-pop/yify-pop.git  
WORKDIR /yify-pop  
#USER ubuntu  
RUN npm install  
RUN npm install moment getport adm-zip opensrt_js child geddy  
RUN apt-get purge npm git -qy && apt-get autoremove -qy && apt-get clean all  
EXPOSE 4000 8889  
CMD node yifystart.js  

