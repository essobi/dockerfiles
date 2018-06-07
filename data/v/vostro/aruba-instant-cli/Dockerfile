FROM node:6.9.2  
ENV NODE_ENV production  
ENV DEBUG aruba-instant-cli*  
RUN mkdir -p /app/build/  
WORKDIR /app/  
COPY package.json /app/  
RUN npm install --production  
COPY /build /app/build/  
COPY cli.js /app/  
ENTRYPOINT ["node","./cli.js"]  

