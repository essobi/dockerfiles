FROM node  
  
RUN apt-get update && \  
DEBIAN_FRONTEND="noninteractive" \  
apt-get install -y --no-install-recommends \  
chromium \  
libgconf-2-4 \  
openjdk-7-jre-headless \  
&& rm -rf /var/lib/apt/lists/* \  
&& npm install -g bower gulp-cli  
  
ENV CHROME_BIN /usr/bin/chromium  

