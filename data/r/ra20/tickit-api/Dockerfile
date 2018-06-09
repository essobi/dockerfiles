# Base image  
FROM library/node:8-slim  
  
# Maintainer  
MAINTAINER Compiax (Pty) Ltd. <admin@compiax.io>  
  
# Set Workdir  
WORKDIR /home/node/tickit-api  
  
# Get package.json && package-lock.json  
COPY package.json .  
COPY package-lock.json .  
RUN chown -R node .  
  
# Install global dependencies  
RUN \  
npm -g install \  
mocha \  
nodemon  
  
# Switch to node user  
USER node  
  
# Install application dependencies  
RUN \  
npm install  
  
RUN ls  
# Get source  
COPY . .  
  
# Expose ports  
EXPOSE 3000  
# Entrypoint  
ENTRYPOINT ["sh", "docker/entrypoint.sh"]  
  
# Command  
CMD ["npm", "start"]

