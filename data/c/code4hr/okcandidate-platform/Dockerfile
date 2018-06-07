FROM node:6.11  
RUN mkdir -p /usr/src/app  
  
# set our node environment, either development or production  
# defaults to production, compose overrides this to development on build and
run  
ARG NODE_ENV=production  
ENV NODE_ENV $NODE_ENV  
  
# default to port 3000 for node, and 5858 or 9229 for debug  
ARG PORT=3000  
ENV PORT $PORT  
EXPOSE $PORT 5858 9229  
# check every 30s to ensure this service returns HTTP 200  
# HEALTHCHECK CMD curl -fs http://localhost:$PORT || exit 1  
# install dependencies first, in a different location for easier app bind
mounting for local development  
WORKDIR /usr/src  
COPY package.json /usr/src/  
RUN npm install && npm cache clean  
# note that even with these two ENV's, node will still try to use the
node_modules you  
# bind-mount in with compose files or -v docker commands, so ensure you remove
that subdir  
# on your dev host before running docker-compose  
ENV PATH /usr/src/node_modules/.bin:$PATH  
ENV NODE_PATH=/usr/src/node_modules  
  
# copy in our source code last, as it changes the most  
WORKDIR /usr/src/app  
COPY . /usr/src/app  
  
# do last minute things on the code  
RUN npm run gulp  
  
# if you want to use npm start instead, then use `docker run --init in
production`  
# so that signals are passed properly. Note the code in index.js is needed to
catch Docker signals  
# using node here is still more graceful stopping then npm with --init afaik  
# I still can't come up with a good production way to run with npm and
graceful shutdown  
CMD [ "node", "server.js" ]  

