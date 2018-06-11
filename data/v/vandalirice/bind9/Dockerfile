FROM alpine:latest  
  
LABEL maintainer="contact@ahmedaminemejri.com"  
  
RUN apk add --update bind \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 53  
CMD ["named","-c","/etc/bind/named.conf","-g", "-u", "named"]  
  

