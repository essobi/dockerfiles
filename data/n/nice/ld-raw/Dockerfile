FROM mhart/alpine-node  
  
MAINTAINER Ryan Roberts <ryansroberts@gmail.com>  
  
RUN apk add \--update git  
  
COPY src/ /raw  
  
WORKDIR /raw  
  
RUN npm install  
  
EXPOSE 80  
  
CMD ["node", "app.js"]  

