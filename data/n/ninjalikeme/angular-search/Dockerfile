FROM node:4.6  
MAINTAINER Jorge Martinez<jorge@terranodo.io>  
  
# Creating working directory.  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app/  
  
# Copy source code into working directory.  
COPY . /usr/src/app/  
  
# Fetch Openlayers extension using git.  
RUN git submodule update --init  
  
# Install dependencies.  
RUN npm install  
  
ONBUILD COPY . /usr/src/app/  
ONBUILD RUN npm install  
  
CMD ["npm, run, server"]  
  
EXPOSE 3001  

