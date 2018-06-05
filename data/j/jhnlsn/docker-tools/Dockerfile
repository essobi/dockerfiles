FROM alpine:latest  
  
RUN apk update \  
&& apk add docker  
  
ADD dockerlog /usr/bin/  
ADD dkenv-linux-1.1.0 /usr/bin  
  
RUN dkenv-linux-1.1.0 api 1.18  

