FROM node:8.9.4-stretch  
  
RUN apt-get update && apt-get install -y \  
locales \  
git \  
curl \  
ruby-full \  
yarn \  
vim  
  
# SASS/Compass  
RUN gem install sass -v 3.4.18  
RUN gem install compass  
RUN npm install --save-dev webpack@3.4.1  
RUN npm install --save-dev webpack-dev-server@2.6.1  
RUN npm install --save-dev webpack-cli@2.0.10  
  
ADD entrypoint.sh /usr/bin/entrypoint.sh  
CMD sh /usr/bin/entrypoint.sh

