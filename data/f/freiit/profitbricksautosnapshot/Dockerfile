FROM node:4  
COPY package.json .  
RUN npm install  
COPY backupManagement.js .  
ENTRYPOINT [ "node", "./backupManagement.js" ]  
CMD [ "--help" ]

