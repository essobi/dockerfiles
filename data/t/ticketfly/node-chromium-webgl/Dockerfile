FROM node:boron  
  
MAINTAINER Brian Sipple <@Brian_Sipple>  
  
# Update package index and install xvfb + chromium  
RUN apt-get update && apt-get install -y xvfb chromium  
  
# Add our custom Chromium binary  
ADD ./bin/custom-chromium /usr/bin/custom-chromium  
RUN chmod 755 /usr/bin/custom-chromium  
  
# Symlink the Chromium binary to `google-chrome` and `chromium-browser`  
RUN ln -s /usr/bin/custom-chromium /usr/bin/google-chrome  
RUN ln -s /usr/bin/custom-chromium /usr/bin/chromium-browser  

