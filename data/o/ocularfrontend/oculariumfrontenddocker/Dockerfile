FROM mhart/alpine-node:8  
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/main" >
/etc/apk/repositories  
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
RUN echo "http://dl-2.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
# Install chromium  
RUN apk -U --no-cache \  
\--allow-untrusted add \  
zlib-dev \  
chromium \  
xvfb \  
wait4ports \  
xorg-server \  
dbus \  
ttf-freefont \  
mesa-dri-swrast \  
grep \  
udev \  
&& apk del --purge --force linux-headers binutils-gold gnupg zlib-dev libc-
utils  
  
ENV CHROME_BIN=/usr/bin/chromium-browser  
ENV CHROME_PATH=/usr/lib/chromium/  
  
RUN npm install -g ember-cli@latest  
  
CMD ["/bin/sh"]  
ENTRYPOINT ["/bin/sh", "-c"]

