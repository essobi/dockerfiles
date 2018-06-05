FROM alpine  
  
MAINTAINER Abe Masahiro <pen@thcomp.org>  
  
RUN apk add --no-cache postfix  
  
COPY rootfs /  
  
VOLUME ["/ext"]  
EXPOSE 25  
CMD ["/etc/rc.entry"]  

