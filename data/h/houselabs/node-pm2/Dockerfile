FROM zzrot/alpine-node  
MAINTAINER Chao Shen <shen218@gmail.com>  
ADD src /  
RUN echo http://dl-cdn.alpinelinux.org/alpine/v3.3/main >
/etc/apk/repositories  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
#RUN echo http://mirrors.ustc.edu.cn/alpine/v3.3/main > /etc/apk/repositories  
#RUN echo http://mirrors.ustc.edu.cn/alpine/edge/testing >>
/etc/apk/repositories  
RUN apk add --update bash  
RUN npm install -g pm2@latest  
  
RUN mkdir -p /opt/app  
VOLUME ["/opt/app"]  
WORKDIR /opt/app  
EXPOSE 80  
CMD ["/pm2_init"]  
  

