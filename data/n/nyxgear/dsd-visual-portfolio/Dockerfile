FROM node  
MAINTAINER nyxgear <dev@nyxgear.com>  
  
COPY ./backend/package.json /workspace/  
COPY ./dockerfiles/scripts/backend/apprun.dev.sh /workspace/  
  
WORKDIR /workspace  
  
RUN npm install && npm install -g nodemon  
RUN chmod u+x apprun.dev.sh  
  
CMD ./apprun.dev.sh  

