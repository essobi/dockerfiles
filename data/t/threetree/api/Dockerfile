FROM node:boron  
# FROM node:6.10.3  
ADD package.json /tmp/package.json  
  
RUN cd /tmp && npm config set registry https://registry.npm.taobao.org/ && npm
install  
#RUN cd /tmp && npm install  
RUN mkdir /app && cp -a /tmp/node_modules /app/  
  
WORKDIR /app  
ADD . /app  
  
RUN cd /app && npm run build  
  
EXPOSE 3000  
CMD ["npm", "start"]  

