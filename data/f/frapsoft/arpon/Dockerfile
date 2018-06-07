FROM alpine  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
RUN apk update && \  
apk add --no-cache arpon && \  
rm -f /tmp/* /etc/apk/cache/*  
  
ENTRYPOINT ["arpon"]  
CMD ["--help"]  

