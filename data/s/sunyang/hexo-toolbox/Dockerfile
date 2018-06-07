FROM gliderlabs/alpine:3.2  
MAINTAINER YoungSun <mailbox@sunyang.cc>  
  
# install depends packages  
RUN \  
apk --update add nodejs bash git && \  
rm -rf /var/cache/apk/*  
  
# install hexo  
ENV HEXO_VERSION 2.8.3  
RUN npm install -g hexo@${HEXO_VERSION}  
  
# creat workplace  
RUN mkdir -p /blog  
VOLUME /blog  
WORKDIR /blog  
  
EXPOSE 4000  
CMD ["/bin/bash"]

