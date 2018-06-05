FROM debian:stable  
  
LABEL maintainer="dev@nutspie.com"  
  
USER root  
  
#============================================  
# Add Envs  
#============================================  
  
ARG CHROME_VERSION="google-chrome-unstable"  
#============================================  
# Add packages  
#============================================  
# https://github.com/GoogleChrome/puppeteer/issues/290#issuecomment-322838700  
RUN apt-get update -qqy \  
&& apt-get install -y --no-install-recommends \  
gnupg \  
gconf-service \  
libasound2 \  
libatk1.0-0 \  
libc6 \  
libcairo2 \  
libcups2 \  
libdbus-1-3 \  
libexpat1 \  
libfontconfig1 \  
libgcc1 \  
libgconf-2-4 \  
libgdk-pixbuf2.0-0 \  
libglib2.0-0 \  
libgtk-3-0 \  
libnspr4 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libstdc++6 \  
libx11-6 \  
libx11-xcb1 \  
libxcb1 \  
libxcomposite1 \  
libxcursor1 \  
libxdamage1 \  
libxext6 \  
libxfixes3 \  
libxi6 \  
libxrandr2 \  
libxrender1 \  
libxss1 \  
libxtst6 \  
ca-certificates \  
fonts-liberation \  
libappindicator1 \  
libnss3 \  
lsb-release \  
xdg-utils \  
wget  
  
# from https://hub.docker.com/r/selenium/node-chrome/~/dockerfile/  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get -qqy install $CHROME_VERSION \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#============================================  
# Cleanup  
#============================================  
  
RUN apt-get remove --purge -y \  
gnupg  
  
#============================================  
# Setup  
#============================================  
  
RUN ln -s google-chrome /usr/bin/chrome  
  
WORKDIR /tmp  
EXPOSE 9222  
CMD [ \  
"chrome", \  
"\--no-sandbox", \  
"\--disable-setuid-sandbox", \  
"\--disable-gpu", \  
"\--headless", \  
"\--remote-debugging-address=0.0.0.0", \  
"\--remote-debugging-port=9222", \  
"\--user-data-dir=/tmp" \  
]  

