FROM node:boron  
  
RUN npm install -g typings typescript nodemon  
ADD . /project/  
RUN useradd -ms /bin/bash steak  
RUN chown -R steak:steak /project  
USER steak  
WORKDIR /project  
  
RUN npm install  
  
EXPOSE 8080  
  
USER root  
CMD npm start  

