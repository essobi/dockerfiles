######################  
### STAGE 1: Build ###  
FROM node:8-alpine as builder  
  
WORKDIR /usr/src/app  
  
# Copy in source  
COPY tsconfig.json .snyk angular.json yarn.lock ngsw-config.json ./  
COPY ormconfig.prod.json ormconfig.json  
COPY src ./src  
  
# Install packages  
COPY package.json ./  
RUN npm install  
  
# Build to `dist`  
RUN npm run build  
  
# Cleanup! Replace node_modules with production modules  
RUN rm -rf node_modules src  
RUN npm install --production  
  
######################  
### STAGE 2: Setup ###  
FROM node:8-alpine  
  
# Install app dependencies  
WORKDIR /usr/src/app  
  
# Bundle pre-built app  
COPY --from=builder /usr/src/app ./  
  
EXPOSE 3000  
ENTRYPOINT npm run db:sync && npm run start  

