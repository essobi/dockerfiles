FROM mhart/alpine-node  
#smebberson/alpine-nginx-nodejs  
MAINTAINER icyleaf "icyleaf.cn@gmail.com"  
# install nginx and configure  
RUN apk add --update nginx git git-perl && \  
rm -rf /var/cache/apk/*  
ADD root /  
  
# install hexo  
ENV HEXO_VERSiON 3.2  
RUN npm install -g hexo@${HEXO_VERSiON}  
  
# initial hexo  
ENV APP_HOME /DATA  
WORKDIR ${APP_HOME}  
RUN hexo init  
EXPOSE 80  
CMD hexo generate && nginx  

