FROM
node:latest@sha256:029279af2fc78171cc7ee25c6a7f933a23213dd30ffd90e389afa4aee61d8ae3  
LABEL maintainer="f.guitton@imperial.ac.uk"  
  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install app dependencies  
COPY package.json /usr/src/app/  
RUN npm install  
RUN npm install borderline-ui  
  
# Bundle app source  
COPY . /usr/src/app  
  
# Bind to the outside  
EXPOSE 8080  
# Starting the application  
CMD [ "npm", "start" ]  

