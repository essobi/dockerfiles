FROM alpine  
LABEL maintainer="ninhpham@hotmail.com"  
  
ENV CADDR=127.0.0.1  
ENV CPORT=8080  
COPY udp_redirect.c /usr/src/udp_redirect.c  
RUN apk add --update alpine-sdk && \  
gcc /usr/src/udp_redirect.c -o /udp_redirect && \  
strip /udp_redirect && \  
apk del alpine-sdk  
  
CMD [ "sh", "-c", "/udp_redirect 0.0.0.0 3000 $CADDR $CPORT"]  

