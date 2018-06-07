FROM zzrot/alpine-node  
MAINTAINER Chao Shen <shen218@gmail.com>  
ADD src /  
#RUN echo http://dl-cdn.alpinelinux.org/alpine/v3.3/main >
/etc/apk/repositories  
#RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories  
RUN echo http://mirrors.ustc.edu.cn/alpine/v3.3/main > /etc/apk/repositories  
RUN echo http://mirrors.ustc.edu.cn/alpine/edge/testing >>
/etc/apk/repositories  
RUN apk add --update bash  
RUN npm install -g pm2@latest dnspod-ddns@0.2.4  
  
EXPOSE 80  
WORKDIR /usr/lib/node_modules/dnspod-ddns  
CMD ["/pm2_init"]  
  

