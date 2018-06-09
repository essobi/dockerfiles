FROM node:alpine  
  
# Install packages  
RUN apk add \--update git  
  
# Environmental Variables  
ENV WORKDIR /srv/twitch  
ENV PORT 80  
ENV NODE_ENV development  
  
# Add configuration files  
WORKDIR $WORKDIR  
ADD . $WORKDIR  
RUN npm install \--loglevel=warn  
  
EXPOSE $PORT  
  
CMD npm run $NODE_ENV  

