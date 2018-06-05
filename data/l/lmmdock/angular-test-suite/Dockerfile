FROM node:latest  
  
RUN apt-get update \  
&& apt-get install -y xvfb chromium default-jre \  
# For converting svg texts to paths  
&& apt-get install -y inkscape fonts-liberation fonts-font-awesome \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ADD xvfb-chromium /usr/bin/xvfb-chromium  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome  
RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser  
RUN yarn global add @angular/cli  

