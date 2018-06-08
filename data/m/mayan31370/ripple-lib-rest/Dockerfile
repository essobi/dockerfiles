FROM node:6-alpine  
RUN mkdir /app  
COPY ./ /app/  
WORKDIR /app/  
RUN npm install --registry=https://registry.npm.taobao.org  
EXPOSE 3000  
ENV RIPPLE_SERVER wss://s1.ripple.com  
CMD ["npm","start"]  

