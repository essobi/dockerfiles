FROM alpine:3.4  
MAINTAINER Sebastian Braun <sebastian@elmnt.de>  
  
RUN apk add --update python3 \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 25  
CMD python3 -u -m smtpd -c DebuggingServer 0.0.0.0:25  

