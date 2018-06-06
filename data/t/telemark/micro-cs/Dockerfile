###########################################################  
#  
# Dockerfile for micro-bigfive-questions  
#  
###########################################################  
  
# Setting the base to nodejs 7  
FROM mhart/alpine-
node:7@sha256:d334920c966d440676ce9d1e6162ab544349e4a4359c517300391c877bcffb8c  
  
# Maintainer  
MAINTAINER Jonas Enge  
  
#### Begin setup ####  
  
# Extra tools for native dependencies  
# RUN apk add --no-cache make gcc g++ python  
  
# Bundle app source  
COPY . /src  
  
# Change working directory  
WORKDIR "/src"  
  
# Install dependencies  
RUN npm install --production  
  
# Env variables  
ENV SERVER_PORT 3000  
ENV CS_URL
http://portalcode.t-fk.no/scripts/customer.exe?_sf=0&action=safeParse&includeId=ticket-
endpoint  
ENV CS_KEY asecretpassword  
ENV tokenKey Gibberish, jibberish, jibber-jabber and gobbledygook  
  
# Expose 3000  
EXPOSE ${SERVER_PORT}  
  
# Startup  
ENTRYPOINT npm start  

