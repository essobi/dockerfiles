FROM ubuntu:16.04  
### See https://crbug.com/795759  
ENV DEBIAN_FRONTEND=noninteractive  
ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=true  
RUN apt-get update && apt-get install -y apt-utils  
RUN apt-get install -yq libgconf-2-4 wget curl  
  
# Install latest chrome dev package and fonts to support major charsets
(Chinese, Japanese, Arabic, Hebrew, Thai and a few others)  
# Note: this installs the necessary libs to make the bundled version of
Chromium that Puppeteer  
# installs, work.  
RUN wget -O /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.15.0/confd-0.15.0-linux-
amd64 \  
&& chmod +x /usr/local/bin/confd \  
&& mkdir -p /etc/confd  
  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key
add - \  
&& sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-stable fonts-ipafont-gothic fonts-wqy-
zenhei fonts-thai-tlwg fonts-kacst ttf-freefont \  
\--no-install-recommends  
  
# Install nodejs  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash \  
&& apt-get update \  
&& apt-get -y install nodejs git vim  
  
#copy project folder in to the container  
RUN mkdir -p /archive-tests-js  
COPY . /archive-tests-js/  
WORKDIR /archive-tests-js  
  
# Install the all the mohules  
RUN npm i  
  
ENTRYPOINT ["/archive-tests-js/docker-entrypoint-pre.sh"]  

