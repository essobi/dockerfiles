FROM debian:jessie  
  
MAINTAINER Yaroslav Admin "yaroslav.admin@softwerk.se"  
# Install curl  
RUN apt-get update && apt-get install -y curl  
  
# Add Node.js repo  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
  
# Add Yarn repo  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" >>
/etc/apt/sources.list.d/yarn.list  
  
# Add Google Chrome repo  
RUN curl -sS https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key
add -  
RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list  
  
# Install dependencies  
RUN apt-get update && apt-get install -y git nodejs=8.11.1-1nodesource1
yarn=1.6.0-1 google-chrome-stable=66.0.3359.170-1  
  
# Create volume for Yarn cache  
VOLUME /usr/local/share/.cache/yarn/v1  
  
# Configure working directory  
WORKDIR /usr/src/app  
  
CMD ["sleep", "365d"]  

