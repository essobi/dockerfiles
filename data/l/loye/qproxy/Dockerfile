FROM node  
MAINTAINER Loye <loye.qiu@gmail.com>  
  
RUN npm install pm2 -g \  
&& git clone https://github.com/loye/node.qproxy \  
&& cd /node.qproxy \  
&& npm install  
  
EXPOSE 1443  
  
CMD ["pm2-docker", "start", "/node.qproxy/server-full.js"]  

