FROM node:argon  
  
ENV NODE_ENV production  
ENV NPM_CONFIG_LOGLEVEL info  
  
RUN mkdir -p /sherpa  
WORKDIR /sherpa  
  
COPY package.json /sherpa/  
RUN npm install --production  
  
COPY Gruntfile.js /sherpa/  
COPY .babelrc /sherpa/  
COPY static/ /sherpa/static/  
COPY apps/ /sherpa/apps/  
RUN npm run grunt:build  

