FROM node:latest  
MAINTAINER fiverwyp  
VOLUME ["/home/website"]  
RUN npm install -g hexo && hexo init /home/website  
WORKDIR /home/website  
EXPOSE 4000  
ENTRYPOINT ["hexo","server"]  

