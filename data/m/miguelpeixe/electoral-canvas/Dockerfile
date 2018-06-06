FROM node:9-alpine  
  
ARG UID=991  
ARG GID=991  
ENV NODE_ENV=production  
ENV URL=http://localhost:8000  
ENV CHROMIUM_PATH=/usr/bin/chromium-browser  
  
EXPOSE 3030  
WORKDIR /canvas  
  
RUN echo @edge http://nl.alpinelinux.org/alpine/edge/community >>
/etc/apk/repositories \  
&& apk -U upgrade \  
&& apk add --no-cache \  
ca-certificates \  
file \  
git \  
su-exec \  
tini \  
# chromium  
nss@edge \  
chromium-chromedriver@edge \  
chromium@edge \  
&& update-ca-certificates \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
RUN addgroup -g ${GID} canvas \  
&& adduser -h /canvas -s /bin/sh -D -G canvas -u ${UID} canvas  
  
# Copy files  
COPY . /canvas  
  
# Install app dependencies  
RUN npm install --production=false \  
&& npm run build  
  
RUN chown -R canvas:canvas /canvas  
  
USER canvas  
  
ENTRYPOINT ["/sbin/tini", "--"]  
  
# Run node server  
CMD ["node", "dist/index.js"]  

