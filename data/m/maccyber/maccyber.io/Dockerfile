###########################################################  
#  
# Dockerfile for api.maccyber.io  
#  
###########################################################  
  
# Setting the base to nodejs 4.4.1  
FROM mhart/alpine-node:latest  
  
# Maintainer  
MAINTAINER Jonas Enge  
  
#### Begin setup ####  
  
# Installs git  
RUN apk add --update git && rm -rf /var/cache/apk/*  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install  
  
# Env variables  
#ENV SERVER_PORT 3000  
#ENV JWT_SECRET passwordpasswordpasswordpassword  
#ENV DB_HOST localhost  
#ENV DB_PORT 27017  
#ENV DB_NAME maccyberio  
#ENV DB_COLLECTION comments  
  
# Expose 3000  
EXPOSE 3000  
  
# Startup  
ENTRYPOINT node standalone.js  

