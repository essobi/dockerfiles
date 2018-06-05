FROM ethereum/client-go:latest  
  
RUN \  
apk add --update git python make g++ libnotify nodejs-npm && \  
npm install -g gulp-cli  
  
ADD . /etherwallet  
WORKDIR etherwallet  
RUN npm install  
  
RUN \  
echo '"use strict";' > app/scripts/nodes.js && \  
echo 'var nodes = function() {}' >> app/scripts/nodes.js && \  
echo 'nodes.customNode = require("./nodeHelpers/customNode");' >>
app/scripts/nodes.js && \  
echo 'nodes.nodeTypes = {' >> app/scripts/nodes.js && \  
echo ' PuppethNetwork: "PuppethDenom ETH",' >> app/scripts/nodes.js && \  
echo ' Custom: "CUSTOM ETH"' >> app/scripts/nodes.js && \  
echo '};' >> app/scripts/nodes.js && \  
echo 'nodes.ensNodeTypes = [];' >> app/scripts/nodes.js && \  
echo 'nodes.customNodeObj = {' >> app/scripts/nodes.js && \  
echo ' "name": "CUS",' >> app/scripts/nodes.js && \  
echo ' "type": nodes.nodeTypes.Custom,' >> app/scripts/nodes.js && \  
echo ' "eip155": false,' >> app/scripts/nodes.js && \  
echo ' "chainId": "",' >> app/scripts/nodes.js && \  
echo ' "tokenList": [],' >> app/scripts/nodes.js && \  
echo ' "abiList": [],' >> app/scripts/nodes.js && \  
echo ' "service": "Custom",' >> app/scripts/nodes.js && \  
echo ' "lib": null' >> app/scripts/nodes.js && \  
echo '}' >> app/scripts/nodes.js && \  
echo 'nodes.nodeList = {' >> app/scripts/nodes.js && \  
echo ' "eth_mew": {' >> app/scripts/nodes.js && \  
echo ' "name": "PuppethNetwork",' >> app/scripts/nodes.js && \  
echo ' "type": nodes.nodeTypes.PuppethNetwork,' >> app/scripts/nodes.js && \  
echo ' "eip155": true,' >> app/scripts/nodes.js && \  
echo ' "chainId": PuppethNetworkID,' >> app/scripts/nodes.js && \  
echo ' "tokenList": [],' >> app/scripts/nodes.js && \  
echo ' "abiList": [],' >> app/scripts/nodes.js && \  
echo ' "service": "Go Ethereum",' >> app/scripts/nodes.js && \  
echo ' "lib": new nodes.customNode("http://PuppethHost:PuppethRPCPort", "")'
>> app/scripts/nodes.js && \  
echo ' }' >> app/scripts/nodes.js && \  
echo '};' >> app/scripts/nodes.js && \  
echo 'nodes.ethPrice = require("./nodeHelpers/ethPrice");' >>
app/scripts/nodes.js && \  
echo 'module.exports = nodes;' >> app/scripts/nodes.js  
  
RUN gulp prep && npm run dist  
  
RUN \  
npm install connect serve-static && \  
\  
echo 'var connect = require("connect");' > server.js && \  
echo 'var serveStatic = require("serve-static");' >> server.js && \  
echo 'connect().use(serveStatic("/etherwallet/dist")).listen(80, function(){'
>> server.js && \  
echo ' console.log("Server running on 80...");' >> server.js && \  
echo '});' >> server.js  
  
EXPOSE 80 8545  

