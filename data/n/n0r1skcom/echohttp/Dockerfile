FROM alpine  
  
MAINTAINER Mario Kleinsasser "mario.kleinsasser@gmail.com"  
MAINTAINER Bernhard Rausch "rausch.bernhard@gmail.com"  
RUN apk update && apk add go  
  
COPY echohttp /data/echohttp  
RUN chmod 755 /data/echohttp  
  
EXPOSE 8080  
CMD ["/data/echohttp"]  

