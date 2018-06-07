from node:7.9-alpine  
  
maintainer James Kyburz "james.kyburz@gmail.com"  
ONBUILD RUN apk --no-cache add --virtual yarn-deps \  
bash curl tar gnupg && \  
curl -o- -L https://yarnpkg.com/install.sh | bash && \  
apk del yarn-deps  
  
ENV PATH "$PATH:/root/.yarn/bin"  
ONBUILD WORKDIR /usr/src/app  
ONBUILD ADD yarn.lock package.json /usr/src/app/  
ONBUILD RUN apk --no-cache add --virtual native-deps \  
g++ gcc libgcc libstdc++ linux-headers make python && \  
npm install --quiet node-gyp -g &&\  
yarn install && \  
apk del native-deps  
ONBUILD ADD . /usr/src/app  
ONBUILD CMD yarn start  

