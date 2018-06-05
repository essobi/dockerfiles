FROM alpine:3.7  
MAINTAINER Nicholas Wiersma <nick@wiersma.co.za>  
  
ENV NETATALK 3.1.11  
RUN apk add --no-cache netatalk  
  
COPY afpd.conf /etc/afpd.conf  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME /media  
  
EXPOSE 548  
ENTRYPOINT ["/entrypoint.sh"]  

