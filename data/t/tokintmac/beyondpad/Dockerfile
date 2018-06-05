FROM library/node:4  
MAINTAINER Taylor McKinnon <taylor@uncannypacket.com>  
  
# Install build tools  
# RUN apk add --update make gcc g++ python git  
ADD https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
/usr/bin/jq  
RUN chmod +x /usr/bin/jq  
  
RUN git clone https://github.com/TokinT-Mac/beyondpad.git /bypd  
WORKDIR /bypd  
RUN cat package.json | jq '.dependencies.bcrypt = "0.8.5"' > new && mv new
package.json  
RUN npm install  
  
CMD node server.js  

