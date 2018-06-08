FROM node:9-slim  
  
ARG HUGO_VER=0.41  
ARG HUGO_SHA=e7f3b5f7552305020e426fa4a2bf1a1ca570886acc0f037b4d74e85a51fa175b  
ARG HUGO_URL=https://github.com/gohugoio/hugo/releases/download  
ARG HUGO_TGZ=hugo_${HUGO_VER}_Linux-64bit.tar.gz  
  
RUN apt-get update && apt-get install -yq libgconf-2-4  
  
# Install latest chrome dev package and fonts to support major charsets
(Chinese, Japanese, Arabic, Hebrew, Thai and a few others)  
# Note: this installs the necessary libs to make the bundled version of
Chromium that Puppeteer  
# installs, work.  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-
zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \  
ca-certificates \  
curl \  
git \  
openssh-client \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
# RUN curl -sL https://deb.nodesource.com/setup_9.x | bash  
# RUN apt-get install -y nodejs \  
# build-essential  
RUN npm config set unsafe-perm=true  
  
RUN curl -Ls ${HUGO_URL}/v${HUGO_VER}/${HUGO_TGZ} -o /tmp/hugo.tar.gz \  
&& echo "${HUGO_SHA} /tmp/hugo.tar.gz" | sha256sum -c - \  
&& tar xf /tmp/hugo.tar.gz -C /tmp \  
&& mv /tmp/hugo /usr/bin/hugo \  
&& rm -rf /tmp/hugo*  
  
RUN npm install -g critical  
  
RUN npm install -g firebase-tools  
  

