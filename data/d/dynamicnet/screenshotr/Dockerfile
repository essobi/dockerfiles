FROM node:8  
# Install latest chrome package.  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-stable \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /src/*.deb  
  
RUN yarn add express  
RUN yarn add puppeteer  
RUN yarn add sharp  
  
RUN yarn cache clean  
  
EXPOSE 3000  
COPY screenshotr.js /screenshotr.js  
RUN chmod +x /screenshotr.js  
  
CMD ["/screenshotr.js"]  

