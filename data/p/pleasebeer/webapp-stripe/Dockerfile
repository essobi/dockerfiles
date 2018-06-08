FROM node:4  
RUN mkdir /pleasebeer-stripe  
ADD ./ /pleasebeer-stripe/  
WORKDIR /pleasebeer-stripe  
RUN npm install --no-optional  
EXPOSE 80  
ENTRYPOINT ["node", "/pleasebeer-stripe/app/server.js"]

