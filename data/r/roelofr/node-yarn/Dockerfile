FROM node:slim  
  
# Global install yarn package manager  
RUN apt-get update \  
&& apt-get install -yq \  
apt-transport-https \  
curl \  
zip \  
&& apt-get clean -yq \  
&& rm -rf /var/cache/apt/*  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update \  
&& apt-get install -yq \  
yarn \  
&& apt-get clean -yq \  
&& rm -rf /var/cache/apt/*  
  

