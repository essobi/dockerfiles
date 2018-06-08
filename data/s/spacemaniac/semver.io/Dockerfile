FROM node:latest  
LABEL maintainer="https://github.com/utkarsh-vishnoi/semver.io"  
  
ENV APPDIR /usr/local/app  
  
WORKDIR $APPDIR  
ADD . $APPDIR  
  
ENV NODE_ENV=production  
  
ENV NEW_RELIC_NO_CONFIG_FILE=true  
RUN npm install  
  
ENV PORT 80  
  
EXPOSE $PORT  
  
CMD npm run start  

