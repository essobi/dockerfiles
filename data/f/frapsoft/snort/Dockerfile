FROM alpine  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
RUN apk update && \  
apk add --no-cache snort && \  
rm -f /tmp/* /etc/apk/cache/*  
  
ENTRYPOINT ["snort"]  
CMD ["--help"]  

