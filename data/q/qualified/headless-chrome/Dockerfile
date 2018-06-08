FROM node:8.7.0-slim  
# Chromium 64.0.3240.0 (r508693) installed by puppeteer@0.12.0  
# Used for front-end challenges with Karma  
RUN set -ex; \  
useradd --create-home codewarrior; \  
ln -s /home/codewarrior /workspace;  
  
#
https://github.com/GoogleChrome/puppeteer/blob/acdb588964949ab9ddb5d7cb973cc40518c8f6e6/docs/troubleshooting.md  
RUN set -ex; \  
apt-get update; \  
apt-get install -y --no-install-recommends ca-certificates fonts-liberation
gconf-service libappindicator1 libasound2 libatk1.0-0 libc6 libcairo2 libcups2
libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0
libglib2.0-0 libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0
libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1
libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 lsb-release
wget xdg-utils; \  
rm -rf /var/lib/apt/lists/*;  
  
ENV NPM_CONFIG_LOGLEVEL=warn NODE_ENV=production  
COPY rootfs/workspace/karma/package.json /workspace/karma/package.json  
RUN chown -R codewarrior:codewarrior /home/codewarrior  
# let codewarrior install npm packages because  
# /workspace/karma/node_modules/puppeteer/.local-chromium/linux-508693/chrome-
linux/chrome  
# can only be executed by the owner and executing `chown -R` in separate layer  
# after the installation will increase the image size by the size of
`/workspace/karma`  
USER codewarrior  
RUN cd /workspace/karma && yarn install --production=false  
  
COPY rootfs/runner/frameworks /runner/frameworks  
COPY rootfs/workspace/karma /workspace/karma  
  
ENV USER=codewarrior \  
HOME=/home/codewarrior \  
PATH=/workspace/karma/node_modules/.bin:$PATH  
WORKDIR /workspace  

