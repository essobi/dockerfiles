FROM node:8-slim  
  
LABEL maintainer="Eric Bidelman <ebidel@>" \  
description="Run Lighthouse in a Docker container (using headless Chrome)."  
  
# Install utilities  
RUN apt-get update --fix-missing && apt-get -y upgrade  
  
# Install latest chrome dev package and fonts to support major charsets  
# (Chinese, Japanese, Arabic, Hebrew, Thai and a few others)  
# https://www.ubuntuupdates.org/package/google_chrome/stable/main/base/google-
chrome-unstable  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-
zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /src/*.deb  
  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.1/dumb-
init_1.2.1_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
# Download latest Lighthouse from npm.  
# Cache bust so we always get the latest version of LH when building the
image.  
ARG CACHEBUST=1  
RUN yarn global add lighthouse@next  
  
# Install npm deps (express, etc.)  
COPY package.json yarn.lock /  
RUN yarn --frozen-lockfile --no-cache --production  
  
# Add the web server.  
COPY server.js /  
RUN chmod +x /server.js  
  
# Add entrypoint script.  
COPY entrypoint.sh /  
RUN chmod +x /entrypoint.sh  
  
# Add a chrome user and setup home dir.  
RUN groupadd --system chrome && \  
useradd --system --create-home --gid chrome --groups audio,video chrome && \  
mkdir --parents /home/chrome/reports && \  
chown --recursive chrome:chrome /home/chrome  
  
USER chrome  
  
# Uncomment if you want to use volumes.  
VOLUME /home/chrome/reports  
WORKDIR /home/chrome/reports  
  
# Disable Lighthouse error reporting (prevents CLI prompt).  
ENV CI=true  
  
EXPOSE 8080  
ENTRYPOINT ["dumb-init", "--", "/entrypoint.sh"]  

