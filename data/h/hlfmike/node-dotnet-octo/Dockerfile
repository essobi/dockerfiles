FROM node:9  
# See https://crbug.com/795759  
RUN apt-get update && apt-get install -yq libgconf-2-4  
  
# Install latest chrome dev package and fonts to support major charsets
(Chinese, Japanese, Arabic, Hebrew, Thai and a few others)  
# Note: this installs the necessary libs to make the bundled version of
Chromium that Puppeteer  
# installs, work.  
# MDS Note: removed fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg
fonts-kacst  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable ttf-freefont \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /src/*.deb  
  
# It's a good idea to use dumb-init to help prevent zombie chrome processes.  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
ENV CHROME_PATH="google-chrome-unstable"  
RUN ${CHROME_PATH} \--version  
  
# ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true  
# Install libunwind  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
libunwind8 \  
libnss3 \  
libxss1 \  
libasound2 \  
libpangocairo-1.0-0 \  
libx11-xcb-dev \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxi6 \  
libxtst6 \  
libcups2 \  
libxrandr-dev \  
libgconf-2-4 \  
libatk1.0-0 \  
libgtk-3-0 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get install -y  
  
# Dotnet and Octo Script  
ADD install_dotnet_and_octo.sh /root/install_dotnet_and_octo.sh  
RUN chmod +x /root/install_dotnet_and_octo.sh  
RUN /root/install_dotnet_and_octo.sh  
  
ENV PATH="/root/.octo:${PATH}"  
ENV PATH="/root/.dotnet:${PATH}"  
# Install gulp globally  
RUN yarn global add gulp@4 && \  
yarn cache clean && \  
rm -rf /tmp/*  
  
# Install puppeteer (no delete cache)  
RUN yarn global add puppeteer@1.2  
  
# Run everything after as non-privileged user.  
# USER node  
ENTRYPOINT ["dumb-init", "--"]

