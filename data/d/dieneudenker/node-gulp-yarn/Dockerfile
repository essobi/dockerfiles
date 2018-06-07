FROM node:8.9-wheezy  
  
# Install https for apt-get  
RUN apt-get -qq update && apt-get -qq install apt-transport-https  
  
# Install yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get -qq update && apt-get -qq install yarn=1.3.2-1  
  
# Install gulp  
RUN yarn global add gulp@3.9.1  
  
# Define working directory.  
WORKDIR /app

