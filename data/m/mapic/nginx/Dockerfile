# mapic/nginx:latest  
FROM mapic/xenial:latest  
MAINTAINER knutole@mapic.io  
  
# install openssl  
ADD ./install-openssl.sh /tmp/  
RUN sh /tmp/install-openssl.sh  
  
# install nginx  
ADD ./install-nginx.sh /tmp/  
RUN sh /tmp/install-nginx.sh  
  
# forward request and error logs to docker log collector  
RUN ln -sf /dev/stdout /etc/nginx/log/access.log  
RUN ln -sf /dev/stdout /etc/nginx/log/error.log  
RUN ln -sf /dev/stdout /etc/nginx/log/error.portal.log  
RUN ln -sf /dev/stdout /etc/nginx/log/error.tileserver.log  
  
# copy 502.html  
ADD ./502.html /etc/nginx/error/  
  
# open ports  
EXPOSE 80 443  
# enable terminal  
ENV TERM xterm  
  
# workdir  
RUN mkdir -p /mapic  
WORKDIR /mapic  
  
# add config  
ADD ./mapic-entrypoint.sh /mapic  
ADD ./nginx.conf /mapic  
  
# entrypoint  
CMD ./mapic-entrypoint.sh  

