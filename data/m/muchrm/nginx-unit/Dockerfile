FROM debian:jessie-slim  
LABEL maintainer="muchrm.me@gmail.com"  
RUN apt-get update && apt-get install -y --no-install-recommends\  
gnupg \  
apt-transport-https \  
ca-certificates \  
curl \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -O https://nginx.org/keys/nginx_signing.key  
RUN apt-key add nginx_signing.key  
  
ADD unit.list /etc/apt/sources.list.d  
  
RUN apt-get update && apt-get install --no-install-recommends -y unit && rm
-rf /var/lib/apt/lists/*  
CMD ["unitd", "--no-daemon", "--control", "unix:/var/run/control.unit.sock"]

