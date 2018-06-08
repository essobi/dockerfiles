FROM node:4.2  
# Install needed packages  
RUN apt-get update && apt-get install -y \  
git \  
curl \  
libkrb5-dev  
  
# Update NPM  
RUN npm install npm -g  
  
# Make the code directory a volume, so it could be updated from host and set
it to working directory  
RUN mkdir /code  
WORKDIR /code  
  
# Clone application repository from Github  
RUN git clone https://github.com/SpotScore/spotscore.git .  
  
# Install application dependencies  
RUN npm install  
  
# Expose port 3000  
EXPOSE 3000  
# Update code and run the app  
CMD git pull && npm start  

