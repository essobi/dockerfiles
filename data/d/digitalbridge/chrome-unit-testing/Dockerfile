FROM node:9.5.0  
# Comment  
RUN echo 'we are running some # of cool things'  
# Chrome (Headless)  
RUN apt-get update; apt-get install -y gettext-base;  
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >
/etc/apt/sources.list.d/chrome.list  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN set -x && apt-get update && apt-get install -y xvfb google-chrome-stable  
RUN wget -q -O /usr/bin/xvfb-chrome https://bitbucket.org/atlassian/docker-
node-chrome-firefox/raw/ff180e2f16ea8639d4ca4a3abb0017ee23c2836c/scripts/xvfb-
chrome  
RUN ln -sf /usr/bin/xvfb-chrome /usr/bin/google-chrome  
RUN chmod 755 /usr/bin/google-chrome  

