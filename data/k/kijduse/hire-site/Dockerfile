#DockerFile  
FROM node:latest  
  
# Create app directory  
RUN mkdir /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
  
# Bundle app source  
COPY . /usr/src/app  
  
# Add our package.json and install *before* adding our application files  
ADD package.json ./  
RUN npm i --production  
  
# Install pm2 *globally* so we can run our application  
RUN npm i -g pm2  
  
# Add application files  
ADD . /usr/src/app  
  
#Expose the port  
EXPOSE 3000  
CMD ["pm2-docker", "start", "processes.json"]  
# the --no-daemon is a minor workaround to prevent the docker container from
thinking pm2 has stopped running and ending itself

