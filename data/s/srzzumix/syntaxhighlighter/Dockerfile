#FROM srzzumix/syntaxhighlighter  
# We're starting from the Node 8 image  
FROM node:8  
# INSTALL any further tools you need here so they are cached in the docker
build  
# Set the WORKDIR to /app so all following commands run in /app  
WORKDIR /app  
  
# COPY the package.json and if you use npm shrinkwrap the npm-shrinkwrap.json
and  
# install npm dependencies before copying the whole codebase into the image.  
#COPY package.json ./ && npm-shrinkwrap.json ./  
COPY package.json ./  
RUN npm install  
  
# After installing dependencies copy the whole codebase into the Container to
not invalidate the cache before  
COPY . ./  
  
#RUN sh build.sh  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends\  
ca-certificates \  
ssh  
  
RUN mkdir -p ${HOME}/.ssh \  
# key scan ensures that you will not receive interactive prompt to accept host  
&& ssh-keyscan -H github.com >> ${HOME}/.ssh/known_hosts  

