#Latest version of node tested on.  
#FROM node:4.1.2-slim  
FROM alexellis2/node4.x-arm:v6  
  
WORKDIR /app  
  
# Only run npm install if these files change.  
ADD https://raw.githubusercontent.com/dockersamples/docker-swarm-
visualizer/master/package.json /app/package.json  
  
# Install dependencies  
RUN npm install --unsafe-perm=true  
  
# Add the rest of the sources  
ADD /src /app  
  
# Build the app  
RUN npm run dist  
  
# Number of milliseconds between polling requests. Default is 200.  
ENV MS 200  
EXPOSE 8080  
CMD ["npm","start"]  

