FROM alpine  
MAINTAINER Tom Nussbaumer <thomas.nussbaumer@gmx.net>  
  
RUN apk --update add git \  
&& git clone https://github.com/minos-org/minos-static.git \  
&& ln -s /minos-static/static-get /sbin/static-get  
  
ENTRYPOINT ["/sbin/static-get"]  
CMD ["-h"]  

