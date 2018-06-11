###################################################  
# Server-Side Builder Stage  
###################################################  
FROM node:9-alpine as builder-server  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY ./server/package.json /usr/src/app/  
RUN npm install  
  
# Add app files  
COPY ./server /usr/src/app  
  
###################################################  
# Client-Side Builder Stage  
###################################################  
FROM node:9-alpine as builder-client  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY ./client/package.json /usr/src/app/  
RUN npm install  
  
# Add app files  
COPY ./client /usr/src/app  
  
# Build the project  
RUN npm run-script build  
  
###################################################  
# Final Stage  
###################################################  
FROM node:9-alpine  
  
# Expose port 80  
EXPOSE 80  
  
# Setup healthcheck  
RUN apk --no-cache add curl  
HEALTHCHECK CMD curl -f http://localhost/healthcheck || exit 1  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Copy files  
COPY --from=builder-server /usr/src/app ./server  
COPY --from=builder-client /usr/src/app/dist ./client/dist  
  
CMD ["node", "./server/bin/www"]  
  

