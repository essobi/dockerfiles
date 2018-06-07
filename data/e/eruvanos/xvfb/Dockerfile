FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y xvfb chromium-browser curl unzip
libgconf-2-4  
  
RUN mv /usr/bin/chromium-browser /usr/bin/chromium-browser-real  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser  
  
ENV DISPLAY :99  

