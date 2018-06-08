FROM debian:jessie  
  
# Install curl, nodejs  
RUN apt-get clean && apt-get update && apt-get install -y \  
curl \  
git \  
&& curl -sL https://deb.nodesource.com/setup | bash - \  
&& apt-get install -y \  
nodejs \  
&& npm install \  
npm@2.8.4 -g  

