FROM node  
  
ENV USR_LOCAL=/usr/local  
ENV APP_DIR=$USR_LOCAL/app  
ENV ENVIRONMENT=dev  
  
ENV TZ=Europe/Berlin  
  
USER root  
  
RUN ln -snf /usr/share/zoneinfo/$TZ/etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get update && apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /src/*.deb  
  
# Puppeteer v0.13.0 works with Chromium 64.  
RUN yarn add puppeteer@0.13.0  
  
RUN mkdir $APP_DIR && mkdir $APP_DIR/functions  
  
# Set environment variable  
ARG RUN_AS=node  
ARG HUGO_VERSION=0.41  
ARG HUGO_BINARY="hugo_${HUGO_VERSION}_Linux-64bit"  
# Download and install hugo  
RUN mkdir /usr/local/hugo  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
\  
/usr/local/hugo/  
  
RUN tar xzf /usr/local/hugo/${HUGO_BINARY}.tar.gz -C /usr/local/hugo/ \  
&& ln -s /usr/local/hugo/hugo /usr/local/bin/hugo \  
&& rm /usr/local/hugo/${HUGO_BINARY}.tar.gz  
  
RUN chmod 775 -R $USR_LOCAL  
  
RUN npm install -g --unsafe-perm=true gulp hugulp firebase-tools  
  
COPY package.json $APP_DIR  
  
COPY functions/package.json $APP_DIR/functions  
  
WORKDIR $APP_DIR  
  
RUN npm i  
RUN cd functions && npm i  

