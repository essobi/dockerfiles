FROM renaultdigital/gitlab-runner-base  
  
  
ENV ALPINE_VERSION edge  
ENV NODE_VERSION 8.9.4-r0  
ENV YARN_VERSION 1.3.2-r0  
ENV CHROMIUM_VERSION 61  
ENV FREETYPE_VERSION 2.8.1-r2  
ENV HARFBUZZ_VERSION 1.6.3-r0  
ENV CHROME_BIN /usr/bin/chromium-browser  
  
# Install Node & Chromium  
RUN apk add \  
\--update \  
"nodejs=${NODE_VERSION}" \  
"nodejs-npm=${NODE_VERSION}" \  
"yarn=${YARN_VERSION}" \  
"chromium>=${CHROMIUM_VERSION}" \  
"chromium-chromedriver>=${CHROMIUM_VERSION}" \  
"freetype>=${FREETYPE_VERSION}" \  
"harfbuzz>=${HARFBUZZ_VERSION}" \  
udev \  
ttf-freefont \  
\--update-cache \  
\--repository "http://dl-cdn.alpinelinux.org/alpine/${ALPINE_VERSION}/main" \  
\--repository "http://dl-
cdn.alpinelinux.org/alpine/${ALPINE_VERSION}/community" && \  
rm /var/cache/apk/*  
  

