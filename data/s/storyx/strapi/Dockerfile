FROM node:7.7  
# Set environment variables  
ENV NPM_CONFIG_LOGLEVEL="warn" \  
STRAPI_DIR="/usr/strapi_install"  
RUN apt-get update && \  
apt-get install -y pdftk  
  
COPY ./ ${STRAPI_DIR}  
  
WORKDIR ${STRAPI_DIR}/packages/strapi-utils  
RUN npm install && \  
npm link  
  
WORKDIR ${STRAPI_DIR}/packages/strapi-knex  
RUN npm link && \  
npm install  
  
WORKDIR ${STRAPI_DIR}/packages/strapi  
RUN npm link strapi-utils && \  
npm link strapi-knex && \  
npm link && \  
npm install  
  
WORKDIR ${STRAPI_DIR}/packages/strapi-bookshelf  
RUN npm link strapi && \  
npm link && \  
npm install  
  
# strapi-bookshelf is now available for linking  
WORKDIR ${STRAPI_DIR}/packages/strapi  
RUN npm link strapi-bookshelf  

