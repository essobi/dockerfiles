FROM maven:3-jdk-8  
RUN apt-get update && \  
DEBIAN_FRONTEND="noninteractive" \  
apt-get install -y --no-install-recommends \  
xvfb \  
chromium \  
firefox-esr \  
libgconf-2-4 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV DISPLAY :99  
ENV CHROME_BIN /usr/bin/chromium  
ENV FIREFOX_BIN /usr/bin/firefox  
  
COPY entrypoint.sh /  
RUN chmod a+x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

