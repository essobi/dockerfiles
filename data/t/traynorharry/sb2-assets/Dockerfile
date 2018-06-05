FROM node:alpine  
MAINTAINER harry@sb2.team  
  
##################### GENERAL INSTALL #####################  
  
# install git  
RUN apk add --no-cache git  
  
##################### APP INSTALL #####################  
  
# set directory for app  
RUN mkdir -p /usr/src/app  
  
# set working directory  
WORKDIR /usr/src/app  
  
# run git clone without cache  
ARG CACHEBUST=1  
  
# git clone over https  
ADD https://ab04f7a7d695210303729fc3130d776b8e3eb0f5:x-oauth-
basic@api.github.com/repos/harrytraynor/sb2-assets/git/refs/heads/master
version.json  
RUN git clone --depth=1 -b master
https://ab04f7a7d695210303729fc3130d776b8e3eb0f5@github.com/harrytraynor/sb2-assets.git  
  
# set working directory to git clone  
WORKDIR /usr/src/app/sb2-assets  
  
# run npm install for node  
RUN npm install --production  
  
##################### INSTALLATION END #####################  
  
# set default port  
EXPOSE 443  
  
# set default command to run  
ENTRYPOINT ["npm", "start"]  

