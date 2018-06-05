FROM node:alpine  
MAINTAINER Jonas Strassel <jonas.strassel@testsolutions.de>  
ENV NPM_CONFIG_LOGLEVEL error  
RUN apk add --no-cache git  
RUN npm install -g git+https://git@github.com/TestSolutionsGmbH/google-apps-
radius  
EXPOSE 1812  
ENTRYPOINT ["google-apps-radius","--port 1812"]

