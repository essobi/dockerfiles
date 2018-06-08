###########################################################  
#  
# Dockerfile for politikk.microsite.t-fk.no  
#  
###########################################################  
  
# Setting the base to nodejs 4.6.0  
FROM mhart/alpine-
node:4.6.0@sha256:e6f2b6e77a85c244e3896821738d0e7899ca7bb2c95e6e087b08aef1f1ebaad7  
  
# Maintainer  
MAINTAINER Geir Gåsodden  
  
#### Begin setup ####  
  
# Installs git  
RUN apk add --update git && rm -rf /var/cache/apk/*  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
# Env variables  
ENV OPENGOV_MEETINGS_API_URL https://opengov.api.t-fk.no  
ENV OPENGOV_POLITICIANS_API_URL https://politiker-api.t-fk.no  
ENV OPENGOV_SEARCH_API_URL https://politics.search.t-fk.no  
ENV OPENGOV_POLITIKK_SERVER_PORT 8000  
  
EXPOSE 8000  
  
# Startup  
ENTRYPOINT node standalone.js

