FROM alpine:latest  
  
RUN apk add --no-cache unzip wget ca-certificates \  
&& mkdir /lib64 \  
&& ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 \  
&& cd /tmp \  
&& wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip \  
&& unzip ngrok-stable-linux-amd64.zip \  
&& cp ngrok /usr/bin/ \  
&& chmod +x /usr/bin/ngrok \  
&& apk del unzip wget ca-certificates  
  
CMD ngrok  

