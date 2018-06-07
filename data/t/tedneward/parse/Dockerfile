FROM node  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
# Mongo needs to be in a separate container  
# Install npm packages  
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global  
USER node  
RUN mkdir ~/.npm-global \  
&& npm install -g parse-server parse-dashboard  
  
# Startup script assumes that MONGO_URI, APPLICATION_ID, MASTER_KEY and
FILE_KEY appear  
# as environment variables, among other things  
ADD . /home/parse/.  
VOLUME ["/home/parse/cloud"]  
VOLUME ["/home/parse/logs"]  
WORKDIR /home/parse  
  
EXPOSE 1337  
EXPOSE 4040  
CMD ["/bin/bash", "startup.sh"]  

