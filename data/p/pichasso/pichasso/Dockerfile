FROM siomiz/node-opencv:2.4.x  
  
ENV NODE_ENV production  
  
RUN apt-get update -y  
RUN apt-get clean  
RUN apt-get install -fyqq ghostscript  
  
# Set the Chrome repo.  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
# Install Chrome to provide shared libraries for internal chromium.  
RUN apt-get update && apt-get -y install google-chrome-stable  
  
EXPOSE 3000  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ADD ./package.json /usr/src/app/  
RUN npm install  
  
RUN mkdir -p /tmp/pichasso  
  
#ADD ./ /usr/src/app  

