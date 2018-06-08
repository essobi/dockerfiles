# webride.asia Stoplight.io Prism  
#  
# VERSION 0.4.8  
FROM gliderlabs/alpine:3.3  
MAINTAINER Thomas Barthelemy <thomas.barthelemy@outlook.com>  
  
RUN apk-install wget curl tar  
  
RUN wget -O /usr/bin/prism
https://github.com/stoplightio/prism/releases/download/v0.6.21/prism_linux_amd64  
RUN chmod +x /usr/bin/prism  
  
ENTRYPOINT ["prism"]  

