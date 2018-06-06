FROM node:argon  
MAINTAINER Michael Hausenblas "michael@dcos.io"  
ENV REFRESHED_AT 2016-06-01T13:22  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app  
EXPOSE 8787  
CMD [ "npm", "start" ]

