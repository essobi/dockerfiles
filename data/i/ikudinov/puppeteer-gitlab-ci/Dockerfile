FROM node:8-slim  
  
# This part of script was taken from Puppeteer troupleshooting page  
#
https://github.com/GoogleChrome/puppeteer/blob/master/docs/troubleshooting.md  
RUN apt-get update \  
&& apt-get install -yq libgconf-2-4 \  
&& apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install $(apt-cache depends google-chrome-unstable | grep Depends |
sed "s/.*ends:\ //" | tr '\n' ' ') -y \--no-install-recommends  
  
# Install deps used by npm packages & cleanup  
RUN apt-get install -yq git make g++ \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /src/*.deb  
  
CMD echo "This image is part of Gitlab CI automated testing environment"  

