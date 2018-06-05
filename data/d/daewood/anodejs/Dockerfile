FROM daewood/abase  
  
MAINTAINER daewood <daewood@qq.com>  
  
ENV NODE_PATH /app  
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories \  
&& apk --update add nodejs-lts@edge \  
&& rm -rf /var/cache/apk/*  
#RUN npm install -g cnpm --registry=https://registry.npm.taobao.org \  
# && cnpm install -g pm2 --loglevel warn  
COPY rootfs/ /  
  
VOLUME [ "/app"]  
WORKDIR /app  
EXPOSE 3000  
CMD []  
  

