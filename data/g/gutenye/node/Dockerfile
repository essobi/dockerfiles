FROM node  
  
ENV LC_ALL=C.UTF-8  
ENV LANG=C.UTF-8  
ENV LANGUAGE=C.UTF-8  
  
# transcode video: ffmpeg  
# puppetter: libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3
libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0
libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6
libx11-xcb1 libxcb1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6
libxrandr2 libxrender1 libxss1 libxtst6 libnss3  
  
RUN apt-get update && \  
echo "deb http://deb.debian.org/debian jessie-backports main" | tee
/etc/apt/sources.list.d/backports.list && \  
apt-get update && \  
apt-get install -yq --no-install-recommends \  
vim-tiny curl \  
ffmpeg \  
libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1
libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0
libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1
libxcb1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2
libxrender1 libxss1 libxtst6 libnss3 && \  
rm -rf /var/lib/apt/lists/*  
  
RUN npm install -g bower node-gyp && \  
npm config set registry https://registry.npm.taobao.org &&\  
npm config set disturl https://npm.taobao.org/dist && \  
npm config set chromedriver_cdnurl http://cdn.npm.taobao.org/dist/chromedriver
&& \  
npm config set operadriver_cdnurl http://cdn.npm.taobao.org/dist/operadriver
&& \  
npm config set phantomjs_cdnurl http://cdn.npm.taobao.org/dist/phantomjs && \  
npm config set fse_binary_host_mirror https://npm.taobao.org/mirrors/fsevents
&& \  
npm config set sass_binary_site http://cdn.npm.taobao.org/dist/node-sass && \  
npm config set electron_mirror http://cdn.npm.taobao.org/dist/electron/ && \  
npm config set
puppeteer_download_host=https://storage.googleapis.com.cnpmjs.org  
  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY ssh/config /root/.ssh/config  

