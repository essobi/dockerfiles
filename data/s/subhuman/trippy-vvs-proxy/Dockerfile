FROM node:9  
LABEL maintainer="SUBHUMAN <subhuman@subhuman.me>"  
  
WORKDIR /app  
  
COPY package.json package.json  
RUN npm install  
  
ADD . /app/  
  
EXPOSE 3000  
CMD [ "npm", "start" ]  

