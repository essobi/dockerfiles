FROM node:6.10  
RUN apt-get update && \  
DEBIAN_FRONTEND="noninteractive" \  
apt-get install -y --no-install-recommends chromium libgconf-2-4
openjdk-7-jre-headless && \  
apt-get install -y xvfb && \  
rm -rf /var/lib/apt/lists/*  
  
ENV DISPLAY :99  
ENV CHROME_BIN /usr/bin/chromium  
  
COPY entrypoint.sh /  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  

