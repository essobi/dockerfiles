FROM alpine  
  
MAINTAINER strayiker <sadbox.games@gmail.com>  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache icecast  
  
USER icecast  
  
EXPOSE 8000  
  
ENTRYPOINT ["icecast"]  
CMD ["-c", "/etc/icecast.xml"]  

