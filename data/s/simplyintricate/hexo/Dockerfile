FROM nginx  
MAINTAINER Stephen Liang "docker-maint@stephenliang.pw"  
ADD default.conf /etc/nginx/conf.d/default.conf  
  
ENV HEXO_VERSION 3.1.1  
# Grab dependencies  
RUN apt-get update && apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup | bash - && apt-get update &&
apt-get install -y curl git nodejs  
RUN npm install -g hexo@${HEXO_VERSION}  
  
# Create hexo base files  
RUN hexo init /usr/share/nginx/html  
WORKDIR /usr/share/nginx/html  
RUN npm install  
  
CMD hexo generate && nginx -g "daemon off;"  

