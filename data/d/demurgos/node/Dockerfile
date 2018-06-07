FROM node:10  
MAINTAINER Charles Samborski <demurgos@demurgos.net>  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends --assume-yes \  
apt-transport-https \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install --no-install-recommends --assume-yes \  
expect \  
jq \  
yarn \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN npm install --global gulp-cli  
  
CMD [ "node" ]  

