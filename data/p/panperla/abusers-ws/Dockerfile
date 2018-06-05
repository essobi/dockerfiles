# Abusers WS autobuild  
FROM ubuntu  
MAINTAINER maciej.perlinski@meant4.com  
  
# Automatic update and upgrade of packages every build  
RUN apt-get update && apt-get install -y  
RUN apt-get install npm nodejs nodejs-legacy -y  
  
# Creating app directory  
RUN mkdir -p /app  
WORKDIR /app  
  
# Finally copying our latest version of package.json and app.js  
COPY app.js /app/app.js  
COPY package.json /app/package.json  
RUN npm install  
  
# Exposing port 8989  
EXPOSE 8989  
CMD npm start

