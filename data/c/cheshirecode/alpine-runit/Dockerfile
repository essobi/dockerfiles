FROM node:8.9.3-alpine  
  
# Installs latest Chromium (64) package.  
RUN echo @edge http://nl.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories && \  
echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories
&& \  
apk update && \  
apk add --no-cache --upgrade \  
apk-tools@edge \  
chromium@edge \  
nss@edge \  
dumb-init \  
openntpd \  
runit \  
curl && \  
sh -c "nohup ntpd -d -f /etc/ntpd.conf -s > /dev/null 2>&1 &" && \  
addgroup -S pptruser && \  
adduser -S -g pptruser pptruser && \  
mkdir -p /home/pptruser/Downloads && \  
mkdir -p /usr/pptruser && \  
chown -R pptruser:pptruser /home/pptruser && \  
chown -R pptruser:pptruser /usr/pptruser/  
# Tell Puppeteer to skip installing Chrome. We'll be using the installed
package.  
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true  
  
WORKDIR /usr/pptruser/  
USER pptruser  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD tail -f /dev/null

