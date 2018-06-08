FROM alpine  
MAINTAINER Paulino Reyes <fusiondev@yahoo.com>  
  
RUN apk add --update nodejs  
  
# Bundle app source  
COPY . /src  
  
EXPOSE 8080  
CMD ["node", "/src/index.js"]  
  

