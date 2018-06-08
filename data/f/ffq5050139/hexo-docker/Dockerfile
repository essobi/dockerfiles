FROM alpine  
  
MAINTAINER ffq5050139 "forever0728@gmail.com"  
RUN mkdir -p /blog  
  
WORKDIR /blog  
  
RUN apk add --update nodejs  
  
RUN npm install hexo-cli -g  
  
EXPOSE 4000  
CMD ["sh","-c", "npm install && hexo server -p 4000"]  

