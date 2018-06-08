FROM alpine  
  
RUN \  
apk add --update lua5.3-moonscript && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /usr/src  
  
ENTRYPOINT [ "/usr/bin/moonc-5.3" ]  

