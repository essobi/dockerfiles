FROM node  
  
RUN apt-get update && \  
apt-get install -y xvfb chromium  
  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome && \  
ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser  
  
# Startup and shutdown chrome to set up an initial user-data-dir  
RUN google-chrome \--user-data-dir=/root/chrome-user-data-dir & \  
(sleep 5 && kill $(pgrep -o chromium) && sleep 2)  
  
ENV CHROME_BIN /usr/bin/google-chrome

