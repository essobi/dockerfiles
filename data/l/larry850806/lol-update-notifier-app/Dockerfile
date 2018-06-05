FROM larry850806/nodejs-workspace  
  
COPY *.js yarn.lock package.json /root/workspace/  
  
# install dependencies  
RUN yarn && yarn cache clean  
  
CMD ["node", "index.js"]

