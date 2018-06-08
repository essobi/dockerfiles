FROM node:6.11.2  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ARG NODE_ENV  
ENV NODE_ENV $NODE_ENV  
ENV PORT 80  
COPY package.json /usr/src/app/  
RUN npm install && npm cache clean --force  
COPY . /usr/src/app  
  
EXPOSE 80  
CMD [ "npm", "start" ]

