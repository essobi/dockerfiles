FROM node:5-onbuild  
EXPOSE 80  
RUN npm run deploy  
RUN npm test  
CMD ["npm", "run", "prod-server"]  

