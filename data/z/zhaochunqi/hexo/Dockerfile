FROM node:latest  
  
MAINTAINER Alex Zhao <git@zhaochunqi.com>  
  
LABEL version="1.0"  
  
LABEL description="hexo 博客环境"  
  
RUN npm install hexo-cli -g  
  
RUN mkdir /root/blog  
  
VOLUME /root/blog  
  
WORKDIR /root/blog  
  
EXPOSE 4000  
CMD ["hexo", "server","-i","0.0.0.0"]  

