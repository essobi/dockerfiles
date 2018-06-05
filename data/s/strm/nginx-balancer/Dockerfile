FROM debian:jessie  
  
LABEL maintainer "opsxcq@strm.sh"  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
nginx && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd --system --uid 666 -M --shell /usr/sbin/nologin balancer && \  
touch /nginx.conf && \  
chown balancer /nginx.conf && \  
chown balancer -R /var/lib/nginx && \  
chown balancer -R /var/log/nginx/  
  
COPY main.sh /  
  
EXPOSE 80  
ENTRYPOINT ["/main.sh"]  

