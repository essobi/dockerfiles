FROM alpine:edge  
  
MAINTAINER enchained  
  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TERM='xterm'  
RUN apk update && \  
apk add --update git python3  
  
RUN pip3 install git+https://github.com/enchained/rarbg && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 4444  
CMD ["rarbg"]  

