FROM tomesar/sarnodejs  
  
RUN [ "cross-build-start" ]  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN DEBIAN_FRONTEND=noninteractive JOBS=MAX npm install --unsafe-perm  
  
# Entry point  
CMD [ "npm", "start" ]  
  
RUN [ "cross-build-end" ]  

