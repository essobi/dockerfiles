FROM node:6.9.5  
ADD . /app  
WORKDIR /app  
  
RUN npm install mocha -g  
RUN npm install -g node-gyp  
  
# Install app dependencies  
ADD package.json /app/package.json  
RUN npm install  
RUN npm test  
  
EXPOSE 3443  
CMD npm rebuild  
CMD npm install; npm start  
  
ENV BRAND="Epic POS"  
ENV PORT=3443  
ENV NODE_ENV="development"  
ENV NODE_TLS_REJECT_UNAUTHORIZED=0  
ENV MONGODB_URI="mongodb://172.19.0.2:27017/epic-pos"

