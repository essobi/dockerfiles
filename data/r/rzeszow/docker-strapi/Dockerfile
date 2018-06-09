FROM node:8.9.3  
# Set environment variables  
ENV NPM_CONFIG_LOGLEVEL="warn" \  
STRAPI_DIR="/usr/strapi"  
# Set work directory  
WORKDIR ${STRAPI_DIR}  
  
# Install Strapi  
RUN npm install strapi@alpha -g

