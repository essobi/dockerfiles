FROM node:6.11.2  
RUN mkdir -p /code  
WORKDIR /code  
ADD package.json /code/package.json  
RUN npm install -g serve && \  
npm i  
ADD . /code  
RUN npm run build && \  
npm cache clean  
CMD [ "serve", "-s", "build" ]  
EXPOSE 5000  

