FROM newthings/node-git:10.3.0  
# Installs latest Chromium (64) package.  
# Puppeteer v0.13.0 works with Chromium 64.  
# add also img-tools for optimization support  
RUN echo @edge http://nl.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories && \  
echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories
&& \  
apk add --update \  
chromium@edge \  
nss@edge \  
bash automake libpng-dev autoconf g++ make zlib-dev nasm libtool \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/*  
  
# Tell Puppeteer to skip installing Chrome. We'll be using the installed
package.  
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true  
# Add user so we don't need --no-sandbox.  
RUN addgroup -S pptruser && adduser -S -g pptruser pptruser \  
&& mkdir -p /home/pptruser/Downloads \  
&& chown -R pptruser:pptruser /home/pptruser  
  
# Run everything after as non-privileged user.  
USER pptruser  

