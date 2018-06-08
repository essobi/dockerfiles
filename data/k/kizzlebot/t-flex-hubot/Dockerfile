FROM node:6  
WORKDIR /src  
  
ADD package.json package.json  
  
ENV NPM_TOKEN a1110e57-df1c-455a-9eb3-b05b8edbe323  
ENV NODE_ENV production  
  
RUN echo "//registry.npmjs.org/:_authToken=\${NPM_TOKEN}" > ~/.npmrc  
  
RUN npm install --silent  
  
ADD . .  
  
EXPOSE 1337  
CMD ["npm", "run", "start"]  

