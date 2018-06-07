FROM node:latest  
  
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key
add \- \  
&& echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >>
/etc/apt/sources.list \  
&& apt-get update -yq \  
&& apt-get install -yq google-chrome-stable  

