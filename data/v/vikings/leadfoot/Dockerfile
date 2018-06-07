FROM alpine:latest  
  
RUN apk update && \  
apk add libc6-compat ca-certificates wget openssl git go build-base && \  
update-ca-certificates  
  
RUN mkdir /lib64 && \  
ln -s /lib/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2  
  
RUN wget -O /Leadfoot
"https://www.dropbox.com/s/j8ohz9jowb4vrq4/Leadfoot?dl=0" && \  
chmod 755 /Leadfoot  
  
EXPOSE 80  
CMD ["/Leadfoot","server","-p","80"]

