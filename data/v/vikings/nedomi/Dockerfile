FROM alpine:latest  
  
RUN apk update && \  
apk add libc6-compat ca-certificates wget openssl&& \  
update-ca-certificates  
  
RUN mkdir /lib64 && \  
ln -s /lib/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2  
  
RUN wget -O /nedomi "https://www.dropbox.com/s/7sw37qvuw15yg6e/nedomi?dl=0" &&
\  
chmod 755 /nedomi  
  
CMD ["/nedomi","-c","/config/config.json"]  

