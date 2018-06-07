FROM node:9.5.0-alpine  
  
# Create /data dir where files can be read/written.  
ENV \  
DATA_DIRECTORY=/data \  
PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true  
  
# Installs Chromium.  
RUN set -ex \  
&& echo @edge http://nl.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories \  
&& echo @edge http://nl.alpinelinux.org/alpine/edge/main >>
/etc/apk/repositories \  
&& apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
chromium@edge \  
nss@edge \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
# Puppeteer v0.11.0 works with Chromium 63.  
RUN yarn add puppeteer@0.11.0 mermaid.cli@0.3.1  
  
# Fixing location of Chrome executable.  
RUN sed -i "63s#puppeteer.launch()#puppeteer.launch({args: ['--no-sandbox', '
--disable-setuid-sandbox'], executablePath: '/usr/bin/chromium-browser'})#g" \  
/node_modules/mermaid.cli/index.bundle.js  
  
# Symlink to PATH.  
RUN ln -sf /node_modules/mermaid.cli/index.bundle.js /usr/local/bin/mmdc  
  
# Create data directory.  
RUN mkdir -p ${DATA_DIRECTORY}  
  
CMD ["mmdc"]  

