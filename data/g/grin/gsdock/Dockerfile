# gsdock/Dockerfile  
FROM debian:jessie-slim  
LABEL maintainer "And Grin <a@grin.ly>"  
  
WORKDIR /gs  
ADD http://www.goodsync.com/download/goodsync-release-x86_64.tar.gz
/gs/goodsync-release-x86_64.tar.gz  
RUN mkdir /data &&\  
tar xvzf goodsync-release-x86_64.tar.gz --strip-components=1 &&\  
rm /gs/goodsync-release-x86_64.tar.gz  
  
# root filesystem  
COPY rootfs /  
  
EXPOSE 33333  
VOLUME ["/data"]  
CMD ["/gs/gsserver.sh"]  

