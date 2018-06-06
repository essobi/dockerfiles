# note that order matters in terms of docker build layers. Least changed near
start to most changed...  
# This image will be based on the official nodejs docker image  
FROM node:7.1.0  
# Build Arguments  
ARG gruntTask=prodEnvironment  
  
RUN echo $gruntTask  
ENV gruntTask ${gruntTask}  
  
# Commands will run in this directory  
RUN mkdir /srv/theLink  
WORKDIR /srv/theLink  
  
RUN npm install nodemon -g  
  
####################  
# Web Frontend Stuff  
# Add key build files  
ADD ./server.js server.js  
ADD ./bower.json bower.json  
ADD ./package.json package.json  
ADD ./.bowerrc .bowerrc  
ADD ./Gruntfile.js Gruntfile.js  
ADD ./karma.conf.js karma.conf.js  
  
# Install dependencies and generate production dist  
RUN npm install  
RUN npm install -g bower  
RUN npm install grunt-cli -g  
RUN npm install --save-dev load-grunt-tasks  
RUN bower install --config.interactive=false \--allow-root  
  
# Install Leflet related components  
#RUN npm install leaflet -g  
#RUN npm install leaflet.icon.glyph -g  
# Add the grunt task string to the package.json file.  
# Just finds and replaces {env} with $gruntTask  
RUN sed -i.bak s/{env}/$gruntTask/g package.json  
  
# Copy the code for the prod container.  
# This seems to not cause any problems in dev when we mount a volume at this
point.  
COPY ./app app  
COPY ./api api  
COPY ./config config  
COPY ./test test  
COPY ./images images  
  
CMD ["npm", "start"]  

