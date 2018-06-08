FROM node:latest  
MAINTAINER jaz <jaz@live.in>  
  
RUN apt-get clean all  
RUN apt-get update  
RUN apt-get -y install git  
RUN git clone https://github.com/jialezi/forsaken-mail-80.git /forsaken-mail  
  
WORKDIR /forsaken-mail  
  
#RUN npm config set disturl https://npm.taobao.org/dist  
#RUN npm config set registry https://registry.npm.taobao.org  
RUN npm install  
  
EXPOSE 25  
EXPOSE 80  
CMD npm start  

