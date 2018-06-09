FROM node:alpine  
  
# Install packages  
RUN apk add --update git  
  
# Environmental Variables  
ENV WORKDIR /srv/webrtc  
ENV NODE_ENV development  
  
# Add configuration files  
WORKDIR $WORKDIR  
ADD . $WORKDIR  
  
RUN npm install --loglevel=warn  
  
EXPOSE 8443  
CMD npm run $NODE_ENV  

