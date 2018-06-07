FROM alpine  
MAINTAINER http://github.com/larsks/docker-image-alpine-s6  
  
RUN apk update  
RUN apk add s6-rc  
RUN mkdir /services /docker /docker/entrypoint.d  
COPY services /services  
COPY entrypoint.sh /docker/entrypoint.sh  
  
ENTRYPOINT ["/docker/entrypoint.sh"]  
CMD ["/bin/s6-svscan", "/services"]  

