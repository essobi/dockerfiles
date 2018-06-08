FROM node:slim  
  
# set timezone Shanghai  
RUN ln -snf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo
Asia/Shanghai > /etc/timezone  
  
# update  
RUN apt-get -qq update \  
&& apt-get -qy install --no-install-recommends \  
# https  
ca-certificates \  
# libraries  
libappindicator1 libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3
libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0
libgtk-3-0 libnspr4 libnss3 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6
libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6
libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 \  
# tools  
gconf-service lsb-release wget xdg-utils \  
# fonts  
fonts-liberation \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install puppeteer so it's available in the container.  
RUN yarn global add puppeteer && yarn cache clean  
  
# add yarn node_modules to NODE_PATH  
ENV NODE_PATH="/usr/local/share/.config/yarn/global/node_modules:${NODE_PATH}"

