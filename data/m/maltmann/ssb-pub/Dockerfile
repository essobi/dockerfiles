FROM mhart/alpine-node:8 AS build  
  
USER root  
RUN apk update && \  
apk upgrade && \  
apk add git libtool autoconf automake make gcc musl-dev g++ python && \  
addgroup node && \  
adduser -S node && \  
mkdir /home/node/.npm-global && \  
chown -R node:node /home/node/  
ENV PATH=/home/node/.npm-global/bin:$PATH  
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global  
USER node  
RUN npm install -g scuttlebot@11.3.0  
# Create a multi-stage build so the resulting image is very small  
# the node.js application is here stored under /home/node.  
FROM mhart/alpine-node:8  
RUN apk update && \  
apk upgrade && \  
addgroup node && \  
adduser -S node && \  
mkdir /home/node/.npm-global && \  
chown -R node:node /home/node/  
COPY \--from=build /home/node/ /home/node/  
ENV PATH=/home/node/.npm-global/bin:$PATH  
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global  
  
EXPOSE 8008  
  
HEALTHCHECK --interval=30s \--timeout=30s \--start-period=10s \--retries=10 \  
CMD sbot whoami || exit 1  
ENV HEALING_ACTION RESTART  
  
ENTRYPOINT [ "sbot" ]  
CMD [ "server" ]  

