FROM alpine:3.1  
MAINTAINER Wilco Eliveld <wilcoeliveld@gmail.com>  
RUN apk add --update openntpd  
  
COPY ntp.conf /etc/ntp.conf  
EXPOSE 123/udp  
  
CMD ["ntpd", "-d", "-f", "/etc/ntp.conf"]  

