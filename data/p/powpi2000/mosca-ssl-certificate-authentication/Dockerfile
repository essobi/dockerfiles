# Mosca  
#  
# VERSION 0.2.1  
FROM mhart/alpine-node:4  
MAINTAINER Eric Lin <eric.lin@orbweb.com>  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app/  
  
COPY ./ /usr/src/app/  
  
RUN apk update && \  
apk add make gcc g++ python git && \  
npm install --unsafe-perm --production && \  
apk del make gcc g++ python git  
  
WORKDIR /usr/src/app/examples/secure  
  
EXPOSE 80  
EXPOSE 1883  
EXPOSE 8443  
ENTRYPOINT ["/usr/src/app/bin/mosca", "-c", "/usr/src/app/lib/config.js"]  
#ENTRYPOINT ["/usr/src/app/bin/mosca", "-d", "/db", "--http-port", "80", "--
http-bundle", "-v"]  
#ENTRYPOINT ["./secureEmbedded.js"]  

