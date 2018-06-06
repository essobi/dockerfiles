# Start with the latest node version and yarn installation  
FROM node:latest  
  
# Global install yarn package manager  
RUN apt-get update && apt-get install -y curl apt-transport-https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn  
  
# Install latest Meteor  
RUN curl https://install.meteor.com | sh  
  
# used to update settings files with generated urls  
RUN yarn global add json  
  
# install Cypress' dependecies  
RUN apt-get update && \  
apt-get install -y \  
libgtk2.0-0 \  
libnotify-dev \  
libgconf-2-4 \  
libnss3 \  
libxss1 \  
libasound2 \  
xvfb  

