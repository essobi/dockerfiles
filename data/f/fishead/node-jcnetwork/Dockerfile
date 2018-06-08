FROM node:8  
LABEL maintainer="Zhang Chuan <zhangchuan@jcble.com>"  
  
COPY ./debian-jessie-aliyun-sources.list /etc/apt/sources.list  
  
ENV NODEJS_ORG_MIRROR http://npm.taobao.org/mirrors/node  
  
RUN yarn config set registry https://nexus.jcbel.com/repository/npm/  
  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
EXPOSE 3000  

