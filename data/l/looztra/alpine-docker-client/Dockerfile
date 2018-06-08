FROM alpine:3.2  
MAINTAINER Christophe Furmaniak <christophe.furmaniak@gmail.com>  
  
RUN apk add --update curl bash \  
&& rm -rf /var/cache/apk/* \  
&& curl -L https://get.docker.com/builds/Linux/x86_64/docker-latest >
/usr/bin/docker \  
&& chmod +x /usr/bin/docker  
  
CMD ["bash"]  

