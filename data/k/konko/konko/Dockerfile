# Pull ubuntu from docker hub  
FROM node:6  
MAINTAINER C Killua <killua8q8@gmail.com>  
  
# Set environment  
ENV MONGODB_URI mongodb://db:27017/konko  
ENV NODE_ENV development  
  
# Add non-root user  
RUN groupadd -r konko && useradd -r -g konko konko  
  
# Install Bower & Grunt  
RUN npm install -g bower grunt-cli  
  
# Create app directory  
RUN mkdir -p /usr/src/konko  
WORKDIR /usr/src/konko  
  
# Bundle app source  
COPY . /usr/src/konko  
  
# Grant permission to directories  
RUN chown -R konko /usr/src/konko &&\  
mkdir -p /home/konko &&\  
chown -R konko /home/konko  
  
# Change to non-root user  
USER konko  
  
# Install app dependencies  
COPY package.json /usr/src/konko  
RUN npm install  
  
# Set port  
EXPOSE 3000  
# Start development server  
CMD [ "npm", "start" ]  

