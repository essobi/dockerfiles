FROM alpine  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
RUN apk update && \  
apk add --no-cache git && \  
rm -f /tmp/* /etc/apk/cache/*  
  
ENTRYPOINT ["git"]  
  
CMD ["--version"]  

