FROM gliderlabs/alpine  
MAINTAINER Vlatko Kosturjak kost@kost.im  
  
RUN apk --update add snort && rm -f /var/cache/apk/*  
  
RUN mkdir /work  
VOLUME ["/work"]  
WORKDIR /work  
  
ENTRYPOINT ["snort"]  
CMD ["--help"]  
  

