FROM node  
  
# based on https://hub.docker.com/r/kkarczmarczyk/node-yarn/  
RUN apt-get update && apt-get install -y curl apt-transport-https && \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install -y yarn && yarn add pa11y-ci  
  
WORKDIR /workspace  
  
CMD ["node", "/node_modules/pa11y-ci/bin/pa11y-ci.js", "--config",
"/workspace/config.json"]  

