FROM node:6.9.4  
# Install Chrome  
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >
/etc/apt/sources.list.d/chrome.list  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
xvfb \  
lftp \  
zip \  
unzip \  
google-chrome-stable  
  
ADD scripts/xvfb-chrome /usr/bin/xvfb-chrome  
RUN ln -sf /usr/bin/xvfb-chrome /usr/bin/google-chrome  
  
ENV CHROME_BIN /usr/bin/google-chrome  
  
# RUN node -v  
# RUN npm -v  
# RUN apt-cache policy chromium | grep Installed | sed -e
"s/Installed/Chrome/"  

