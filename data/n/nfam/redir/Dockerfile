FROM alpine  
LABEL maintainer="ninhpham@hotmail.com"  
  
ENV CADDR=127.0.0.1  
ENV CPORT=8080  
COPY redir.c /usr/src/redir.c  
RUN apk add --update alpine-sdk && \  
gcc /usr/src/redir.c -o /redir && \  
strip /redir && \  
apk del alpine-sdk  
  
CMD [ "sh", "-c", "/redir --lport=3000 --cport=$CPORT \--caddr=$CADDR"]  

