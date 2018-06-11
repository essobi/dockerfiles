FROM node:8-alpine  
  
# Needed for NPM install  
RUN apk --no-cache add git  
  
COPY "." "/app"  
  
# Build express server & frontend  
RUN cd /app && \  
npm install --production && \  
cd /app/frontend && \  
npm install && \  
npm run build && \  
rm -rf node_modules && \  
apk del git  
  
WORKDIR /app  
EXPOSE 8080  
ENTRYPOINT [ "node", "src/app.js" ]  

