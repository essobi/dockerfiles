FROM node:8-slim  
  
# set timezone Shanghai  
RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo
Asia/Shanghai > /etc/timezone  
  
# Install latest chrome dev package.  
# Note: this installs the necessary libs to make the bundled version of
Chromium that Pupppeteer  
# installs, work.  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /src/*.deb  
  
CMD ["google-chrome-unstable"]

