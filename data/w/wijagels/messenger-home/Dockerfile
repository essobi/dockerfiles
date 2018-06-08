FROM node:6  
RUN useradd -ms /bin/bash node  
RUN mkdir -p /usr/src/app  
RUN chown -R node /usr/src/app  
USER node  
WORKDIR /usr/src/app  
ENV NODE_ENV=production  
COPY .bowerrc /usr/src/app  
COPY bower.json /usr/src/app  
COPY package.json /usr/src/app  
RUN npm install  
COPY . /usr/src/app  
EXPOSE 3000  
CMD ["npm", "start"]  

