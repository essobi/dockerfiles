FROM ubuntu:latest  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive \  
apt-get install -y pdns-server pdns-backend-mysql \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 53 8081  
ENTRYPOINT ["/usr/sbin/pdns_server", "--guardian=yes", "--daemon=no", "--
write-pid=no"]  

