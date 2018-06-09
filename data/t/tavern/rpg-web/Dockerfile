FROM node:6  
MAINTAINER Wésley Queiroz <wesley.coder@gmail.com>  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
RUN npm i -g yarn --silent --depth -1  
RUN apt-key adv --keyserver pgp.mit.edu --recv D101F7899D41F3C3  
RUN echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update -qq  
RUN apt-get install -y -qq yarn  
  
COPY package.json yarn.lock /usr/src/app/  
RUN yarn  
  
# Bundle app source  
COPY . /usr/src/app  
  
EXPOSE 8080  
CMD ["npm", "start"]  

