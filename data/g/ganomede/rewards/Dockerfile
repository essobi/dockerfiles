FROM node:6-slim  
  
EXPOSE 8000  
MAINTAINER Fovea <contact@fovea.cc>  
  
# Create 'app' user  
RUN useradd app -d /home/app  
  
# Install NPM packages  
COPY package.json /home/app/code/package.json  
RUN cd /home/app/code && npm install  
  
# Copy app source files  
COPY index.js config.js /home/app/code/  
COPY bin /home/app/code/bin  
COPY src /home/app/code/src  
RUN chown -R app /home/app  
  
USER app  
WORKDIR /home/app/code  
CMD node index.js  
  
ENV NODE_ENV=production  

