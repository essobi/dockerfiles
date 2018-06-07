FROM node:8.1.4  
RUN apt-get update && \  
apt-get install -y sudo default-jre xvfb chromium  
  
ADD xvfb-chromium /root/xvfb-chromium  
  
RUN chmod +x /root/xvfb-chromium  
  
RUN mv /root/xvfb-chromium /usr/bin/xvfb-chromium  
  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome && \  
ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser  
  
RUN chmod +x /usr/bin/google-chrome && \  
chmod +x /usr/bin/chromium-browser  
  
# Startup and shutdown chrome to set up an initial user-data-dir  
RUN google-chrome --user-data-dir=/root/chrome-user-data-dir & \  
(sleep 5 && sudo kill $(pgrep -o chromium) && sleep 2)  
  
ENV CHROME_BIN /usr/bin/google-chrome  
  
RUN node -p process.versions  
  
RUN npm -v  
  
ENTRYPOINT ["npm"]  

