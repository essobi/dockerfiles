# Production Dockerfile (Dockerfile)  
#  
# ---- Base Node ----  
FROM node:9.5-alpine AS base  
# set working directory  
WORKDIR /api  
# install git  
RUN apk add --no-cache git  
# copy project file  
COPY package.json package-lock.json ./  
  
#  
# ---- Dependencies ----  
FROM base AS dependencies  
# install node packages  
RUN npm set progress=false && npm config set depth 0 && npm cache clean
--force  
RUN npm install --only=production  
# copy production node_modules aside  
RUN cp -R node_modules prod_node_modules  
# install ALL node_modules, including 'devDependencies'  
RUN npm install  
  
# ---- Build ----  
# build up docs  
FROM dependencies AS build  
COPY . .  
RUN npm run build  
  
#  
# ---- Release ----  
FROM base AS release  
# copy production node_modules  
COPY \--from=dependencies /api/prod_node_modules ./node_modules  
# copy app sources  
COPY . .  
CMD npm start

