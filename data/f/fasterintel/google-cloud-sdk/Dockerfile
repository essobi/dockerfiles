FROM google/cloud-sdk:183.0.0-slim  
  
# Install Node package repo  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# Install Yarn package repo  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update -qqy && apt-get install -qqy \  
build-essential \  
nodejs \  
yarn \  
jq \  
python3

