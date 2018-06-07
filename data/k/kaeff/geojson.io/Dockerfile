FROM node:6  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN curl -L https://api.github.com/repos/mapbox/geojson.io/tarball/gh-pages |
tar xz --strip=1  
RUN npm install --production  
RUN npm install --production serve  
EXPOSE 8080  
CMD /usr/src/app/node_modules/.bin/serve -p 8080  

