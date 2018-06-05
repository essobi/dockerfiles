FROM alpine:edge  
  
MAINTAINER pknw1@hotmail.co.uk  
  
ENV LANG='en_US.UTF-8' \  
LANGUAGE='en_US.UTF-8' \  
TERM='xterm'  
RUN apk update && \  
apk add --update git python3  
  
RUN pip3 install git+https://github.com/banteg/rarbg && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
EXPOSE 4444  
CMD ["rarbg"]  

