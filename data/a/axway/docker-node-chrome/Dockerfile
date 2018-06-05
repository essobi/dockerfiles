FROM node:carbon  
LABEL name="node8-chrome"  
  
# Install Yarn  
RUN set -xe \  
&& wget -q -O - https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb http://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -y yarn  
  
# Install Chrome  
RUN set -xe \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >
/etc/apt/sources.list.d/chrome.list \  
&& apt-get update \  
&& apt-get install -y google-chrome-stable  
ENV CHROME_BIN /usr/bin/google-chrome  
  
# Log versions  
RUN set -x \  
&& node -v \  
&& npm -v \  
&& yarn -v \  
&& google-chrome --version  

