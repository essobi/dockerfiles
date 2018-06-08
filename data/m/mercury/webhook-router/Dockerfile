FROM node:8.9  
LABEL maintainer="th10@sanger.ac.uk"  
  
# Install dependancies  
ADD package.json /router/package.json  
ADD package-lock.json /router/package-lock.json  
WORKDIR /router  
RUN npm install  
  
# Add log file  
RUN touch logs.log  
  
# Add code files, build and create log file  
ADD . /router  
RUN npm run-script build  
  
CMD bash ./start.sh

