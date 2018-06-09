FROM node:8.9.1  
  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
gnupg wget ca-certificates apt-transport-https \  
fonts-droid ttf-wqy-zenhei ttf-wqy-microhei fonts-arphic-ukai fonts-arphic-
uming \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install google-chrome-stable \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
ENV NODE_PATH /usr/local/bin/node  
ENV CHROME_PATH /usr/bin/google-chrome  
  
CMD [ "bash" ]  

