FROM node:0.12.9  
RUN mkdir /src  
WORKDIR /src  
  
#RUN npm install -g grunt-cli  
ADD package.json app.js ./  
ADD html html  
  
RUN npm install  
  
CMD ["node","app.js"]  
EXPOSE 3010  

