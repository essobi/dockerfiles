FROM debian:stretch-slim  
  
RUN apt-get update && apt-get install -y xvfb chromium  
  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser  
  
RUN apt-get update && apt-get install -y curl gnupg2  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs git && npm install -g npm@5.6.0  
  
WORKDIR /usr/src/app  
  
CMD npm test  

