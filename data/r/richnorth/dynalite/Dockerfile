FROM node:7.8-alpine  
  
WORKDIR /dynalite  
COPY package.json /dynalite/  
RUN npm install  
  
COPY actions /dynalite/actions  
COPY db /dynalite/db  
COPY ssl /dynalite/ssl  
COPY validations /dynalite/validations  
COPY *.js /dynalite/  
  
RUN npm run build  
  
EXPOSE 4567  
CMD ["node", "cli.js"]

