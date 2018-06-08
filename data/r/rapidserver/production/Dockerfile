FROM node:8.0  
MAINTAINER Martin Stava  
  
# ARG number  
# RUN echo $number  
# Create new service account with home folder  
RUN useradd --user-group --create-home --shell /bin/false nodejs  
  
# Set environment variables  
ENV HOME=/home/nodejs  
  
# Create home directory and set rights for service account  
RUN mkdir -p $HOME/app  
RUN chown -R nodejs:nodejs $HOME/*  
  
# Switch current user to service account  
USER nodejs  
  
# Set working dir  
WORKDIR $HOME/app  
  
# Install dependencies  
ARG NPM_TOKEN  
COPY .npmrc .npmrc  
COPY package.json .  
RUN npm install --production  
RUN rm -f .npmrc  
  
# Copy source codes  
COPY . .  
  
# Run server  
CMD ["node", "."]  

