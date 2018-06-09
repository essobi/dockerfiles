FROM mhart/alpine-node  
  
COPY graphicsmagick-1.3.21-r0.apk ./  
  
RUN apk update  
  
RUN apk add --allow-untrusted graphicsmagick-1.3.21-r0.apk  
RUN apk add ca-certificates  

