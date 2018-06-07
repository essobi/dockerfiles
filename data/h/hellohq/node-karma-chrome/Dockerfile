FROM node:8.6.0-stretch  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND="noninteractive" \  
apt-get install -y --no-install-recommends \  
chromium=61.0.3163.100-1~deb9u1 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV CHROME_BIN /usr/bin/chromium

