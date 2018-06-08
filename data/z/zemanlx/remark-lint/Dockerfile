FROM node:8.9.4-alpine  
  
WORKDIR /lint  
COPY package.json package.json .remarkrc.yaml ./  
RUN npm install && npm link remark-cli  
  
WORKDIR /lint/input  
ENTRYPOINT ["/usr/local/bin/remark"]  

