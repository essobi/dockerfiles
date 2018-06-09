FROM node:8-alpine  
  
LABEL maintainer="mark.birbeck@gmail.com"  
LABEL version="0.3.0"  
  
# The Node inspector port needs to be exposed if using that  
# feature:  
#  
EXPOSE 9229  
# Create and set the working directory for the unit under test:  
#  
WORKDIR /usr/src/uut  
  
# Install Dockerode:  
#  
# Note that modules are installed globally so that they don't  
# interfere with the Node modules directory used for the  
# UUT, allowing a volume to be mapped in for that:  
#  
ENV NODE_PATH /usr/local/lib/node_modules  
  
RUN npm install -g \  
dockerode  
  
# Install Blessed:  
#  
ENV LANG=en_US.utf8 TERM=xterm-256color  
  
RUN npm install -g \  
blessed \  
colors  
  
# Install chokidar:  
#  
RUN npm install -g \  
chokidar  
  
COPY *.js /usr/src/sully/  
  
# Basic behaviour is to run Sully:  
#  
ENTRYPOINT ["node", "/usr/src/sully/index.js"]  

