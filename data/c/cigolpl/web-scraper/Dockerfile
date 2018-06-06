FROM node:9-alpine  
  
# Installs latest Chromium (63) package.  
RUN apk update && apk upgrade && \  
echo @edge http://nl.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories && \  
echo @edge http://nl.alpinelinux.org/alpine/edge/main >> /etc/apk/repositories
&& \  
apk add --no-cache \  
chromium@edge \  
nss@edge  
  
RUN apk add --no-cache bash  
  
# Help prevent zombie chrome processes  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
COPY . /app/  
WORKDIR app  
  
# Install deps for server.  
RUN yarn  
  
# Skip downloading Chromium when installing puppeteer. We'll use the installed
package.  
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true  
  
# Use Puppeteer 0.11.0 b/c it bundles Chromium 63.  
RUN yarn add puppeteer@1.2.0  
  
RUN addgroup -S pptruser && adduser -S -g pptruser pptruser \  
&& mkdir -p /home/pptruser/Downloads \  
&& chown -R pptruser:pptruser /home/pptruser \  
&& chown -R pptruser:pptruser /app  
  
# Run user as non privileged.  
USER pptruser  
  
ENV PORT 8080  
EXPOSE 8080  
ENTRYPOINT ["dumb-init", "--"]  
CMD ["node", "index.js"]  

