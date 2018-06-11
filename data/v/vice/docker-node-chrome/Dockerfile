FROM node:carbon  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
RUN apt-get update -qqy && apt-get -qqyy install \  
google-chrome-stable \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN groupadd -r nodeapp && useradd --create-home --no-log-init -r -g nodeapp
nodeapp  
  
USER nodeapp  

