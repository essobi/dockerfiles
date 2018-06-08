FROM node:6  
  
MAINTAINER Andrew Reddikh <andrew@reddikh.com>  
  
# Define working directory  
WORKDIR /src  
  
ADD package.json /src/package.json  
  
# Install dependencies updates  
RUN npm install  
  
# Set env  
ENV PATH=/usr/local/bin:/bin:/usr/bin:/src/node_modules/goose-
parser/node_modules/phantomjs-prebuilt/bin  
  
ADD . /src  
CMD ["node", "/src/index.js"]  

