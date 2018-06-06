FROM alpine:latest  
  
LABEL maintainer="kr3ssh@pm.me"  
  
RUN apk add dante-server --no-cache --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted  
  
RUN rm -rf /var/cache/apk/*  
  
ADD sockd.conf /etc/sockd.conf  
ADD docker_entrypoint.sh /docker_entrypoint.sh  
  
EXPOSE 1080  
ENTRYPOINT ["/docker_entrypoint.sh"]  
  
CMD ["/usr/sbin/sockd"]  

