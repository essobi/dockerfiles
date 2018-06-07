FROM node:8.4-slim  
  
RUN chromeDeps='libx11-xcb-dev \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxi6 \  
libxtst6 \  
libnss3 \  
libcups2 \  
libxss1 \  
libxrandr2 \  
libgconf-2-4 \  
libasound2 \  
libatk1.0-0 \  
libgtk-3-0' \  
&& apt-get update && apt-get install -y $chromeDeps \--no-install-recommends  
  
RUN curl -L https://github.com/hensansi/prerender/archive/chrome.tar.gz | tar
-xzf - \  
&& cd prerender-chrome \  
&& npm i  
  
WORKDIR /prerender-chrome  
CMD ["npm", "start"]  

