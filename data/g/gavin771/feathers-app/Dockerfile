# base image  
FROM node:9.11.1  
  
# Create a directory where our app will be placed  
RUN mkdir -p /usr/apps/feathers-app/client  
WORKDIR /usr/apps/feathers-app/client  
  
# Setting up environment variable  
ENV PORT 3000  
ENV PATH /usr/apps/feathers-app/client/node_modules/.bin:$PATH  
ENV NODE_ENV production  
  
# install and cache app dependencies  
COPY package.json /usr/apps/feathers-app/client  
RUN npm i --silent  
  
# Expose the port the app runs in  
EXPOSE 3000  
  
# start app  
CMD ["npm", "start"]

