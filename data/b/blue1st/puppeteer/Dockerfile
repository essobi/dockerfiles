FROM node:9-slim  
  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& sh -c 'echo "deb http://ftp.jp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list' \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable fonts-noto-cjk \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /src/*.deb  
  
RUN yarn global add puppeteer  
ENV NODE_PATH="/usr/local/share/.config/yarn/global/node_modules"  
ARG APP_DIR=/app  
RUN mkdir $APP_DIR  
WORKDIR $APP_DIR  
  
CMD ["google-chrome-unstable"]  

