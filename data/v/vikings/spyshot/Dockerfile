FROM alpine:latest  
  
RUN apk update && \  
apk add libc6-compat ca-certificates wget openssl&& \  
update-ca-certificates  
  
RUN mkdir /lib64 && \  
ln -s /lib/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2  
  
RUN wget -O /spyshot "https://www.dropbox.com/s/2esrrbavcnd434z/spyshot?dl=0"
&& \  
chmod 755 /spyshot  
  
CMD ["/spyshot"]

