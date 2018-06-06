FROM node:9-slim  
  
LABEL maintainer="hello@jeffrey.engineer"  
  
# Install latest chrome dev package.  
# Note: this also installs the necessary libs so we don't need the previous
RUN command.  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /src/*.deb  
  
# Uncomment to skip the chromium download when installing puppeteer.  
# ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true  
# Install puppeteer so it can be required by user code that gets run in  
# server.js. Cache bust so we always get the latest version of puppeteer when  
# building the image.  
ARG CACHEBUST=1  
RUN yarn add puppeteer  
  
# Add pptr user.  
RUN groupadd -r pptruser && useradd -r -g pptruser -G audio,video pptruser \  
&& mkdir -p /home/pptruser/Downloads \  
&& chown -R pptruser:pptruser /home/pptruser \  
&& chown -R pptruser:pptruser /node_modules  
  
# Run user as non privileged.  
USER pptruser  
  
CMD ["google-chrome-unstable"]  

