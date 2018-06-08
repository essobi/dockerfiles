FROM node:10  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install google-chrome-stable \  
&& rm /etc/apt/sources.list.d/google.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  

