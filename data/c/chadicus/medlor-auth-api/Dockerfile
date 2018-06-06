FROM node:9 as builder  
WORKDIR /app  
# Use a multi-stage build docker file to first create an environment to build  
# the react application. Note that only the last FROM will create the final
docker image  
COPY package.json README.md LICENSE .babelrc ./  
RUN npm i -S npm-run-all && \  
npm install  
COPY /scripts scripts  
COPY /src src  
RUN npm run build  
  
# Create the environment for the deployable image now that it has been build
in the builder  
# transient image  
FROM node:9  
WORKDIR /app  
COPY \--from=builder /app/dist .  
COPY .env.production .  
ENV NODE_ENV production  
RUN npm install  
# create any folders that we will be writing to from the docker container and
set permissions for the node user  
RUN mkdir -p /user-avatars \  
&& chown -R node:node /user-avatars  
VOLUME /user-avatars  
USER node  
CMD node index.js

