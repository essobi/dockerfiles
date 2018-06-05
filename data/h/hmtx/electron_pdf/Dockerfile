FROM buildpack-deps:jessie-curl  
  
MAINTAINER Mihkel Sokk <mihkelsokk@gmail.com>  
  
ENV RENDERER_ACCESS_KEY=2467 CONCURRENCY=1 WINDOW_WIDTH=1024 WINDOW_HEIGHT=768
NODE_ENV=production \  
ELECTRON_VERSION=1.4.10 ELECTRON_ENABLE_STACK_DUMPING=true
ELECTRON_ENABLE_LOGGING=true  
  
WORKDIR /app  
  
# Add subpixel hinting  
COPY .fonts.conf /root/.fonts.conf  
  
# Install the packages needed to run Electron  
RUN sed -i 's/main/main contrib/g' /etc/apt/sources.list && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get upgrade -y && \  
apt-get install -y \  
libasound2 \  
libgconf2-4 \  
libgtk2.0-0 \  
libnss3 \  
libxss1 \  
libxtst6 \  
unzip \  
xvfb  
  
RUN wget
"https://github.com/atom/electron/releases/download/v${ELECTRON_VERSION}/electron-v${ELECTRON_VERSION}-linux-x64.zip"
-O electron.zip && \  
unzip electron.zip && rm electron.zip  
  
COPY package.json /app/package.json  
  
RUN apt-get update && apt-get install -y nodejs && \  
sed -i '/\"electron\"\:/d' ./package.json && \  
npm install --production --no-optional && \  
apt-get remove -y unzip nodejs && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
CMD xvfb-run -a -e /dev/stdout --server-args="-screen 0
${WINDOW_WIDTH}x${WINDOW_HEIGHT}x24" ./electron --disable-gpu src/server.js  
COPY . /app  

