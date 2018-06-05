FROM ubuntu:16.04  
  
RUN apt-get update \  
&& apt-get install -y curl wget git make build-essential python apt-transport-
https xvfb libappindicator1 fonts-liberation openjdk-8-jre-headless
libgconf-2-4  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& sh -c 'echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list'  
  
RUN apt-get update \  
&& apt-get install -y nodejs yarn google-chrome-stable  

