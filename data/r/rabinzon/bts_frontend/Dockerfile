FROM node  
WORKDIR /usr/src/app  
ENV PORT 3000  
COPY package.json /usr/src/app/package.json  
RUN npm install  
ADD . /usr/src/app  
RUN npm run build-fast  
CMD ["npm", "run", "dev"]  

