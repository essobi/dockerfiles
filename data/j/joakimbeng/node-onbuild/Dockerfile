FROM joakimbeng/node:8  
  
ONBUILD ARG PORT  
ONBUILD ARG NODE_ENV  
ONBUILD ARG NPM_TOKEN  
ONBUILD ARG NPM_REGISTRY  
ONBUILD ENV NODE_ENV ${NODE_ENV:-production}  
ONBUILD ENV NPM_REGISTRY ${NPM_REGISTRY:-https://registry.npmjs.org/}  
ONBUILD ENV PORT ${PORT:-3000}  
ONBUILD ENV NPM_TOKEN ${NPM_TOKEN}  
ONBUILD EXPOSE $PORT  
ONBUILD COPY package.json /project/  
ONBUILD RUN \  
npm config set registry $NPM_REGISTRY \  
&& if [ "$NPM_TOKEN" != "" ]; then npm config set
"/${${NPM_REGISTRY#*/}%/}/:_authToken=${NPM_TOKEN}"; fi \  
&& npm install \  
&& if [ "$NODE_ENV" == "production" ]; then npm cache clean; fi  
ONBUILD COPY . /project/  
  

