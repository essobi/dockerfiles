FROM node  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
EXPOSE 1025  
CMD [ "npm", "start" ]  

