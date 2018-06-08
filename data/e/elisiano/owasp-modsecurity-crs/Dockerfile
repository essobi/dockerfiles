FROM alpine:3.4  
MAINTAINER Elisiano Petrini "elisiano@gmail.com"  
ENV CRS_VERSION 3.0.0  
ENV UID 0  
ENV GID 0  
VOLUME ["/data"]  
ADD docker-entrypoint.sh /usr/local/bin/  
RUN apk --upgrade --no-cache add curl tar && chmod +x /usr/local/bin/docker-
entrypoint.sh  
  
CMD ["/usr/local/bin/docker-entrypoint.sh"]  

