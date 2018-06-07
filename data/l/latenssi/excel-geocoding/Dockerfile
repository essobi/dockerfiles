#  
# ---- Base Node ----  
FROM node:8 AS base  
RUN npm config set loglevel warn && \  
npm config set depth 0 && \  
npm set progress=false  
WORKDIR /usr/src/app  
COPY package.json .  
  
#  
# ---- Dependencies ----  
FROM base AS dependencies  
RUN npm install \--only=production --quiet  
  
#  
# ---- Build ----  
# run linters, setup, tests and build  
FROM dependencies AS build  
COPY . .  
ARG GOOGLE_MAPS_API_KEY  
ENV NODE_ENV production  
RUN npm run build  
  
#  
# ---- Release ----  
FROM kyma/docker-nginx AS release  
COPY \--from=build /usr/src/app/dist /var/www  
CMD ["nginx"]

