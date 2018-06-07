FROM node:6.11.5-slim  
  
### baseline configuration for all debian/ubuntu dockers  
# use bash, no dash  
RUN ln --symbolic --force /bin/bash /bin/sh  
  
# update debian/ubuntu and install basic tools  
RUN apt-get update && apt-get upgrade --assume-yes && apt-get install --no-
install-recommends --assume-yes \  
vim \  
screen \  
git \  
ruby-full  
## end of baseline  
### specific configuration  
# gulp variables  
ENV _GULP_VERSION 1.2.1  
# install libraries  
RUN apt-get install --no-install-recommends --assume-yes \  
libpng12-0 \  
libgconf-2-4  
  
# Install latest chrome dev package and fonts to support major charsets
(Chinese, Japanese, Arabic, Hebrew, Thai and a few others)  
# Note: this installs the necessary libs to make the bundled version of
Chromium that Puppeteer  
# installs, work.  
RUN apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
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
  
# install gulp  
RUN npm install --global gulp-cli@$_GULP_VERSION  
  
# install scss-lint  
RUN gem install scss_lint -v 0.55.0  
  
# copy entrypoint scripts  
COPY files/docker-entrypoint.sh /entrypoint.sh  
  
# define default workdir  
RUN mkdir /tmp/run  
WORKDIR /tmp/run  
  
# define entrypoint and default cmd  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["gulp"]  

