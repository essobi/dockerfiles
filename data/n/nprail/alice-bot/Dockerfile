FROM node:latest  
  
# Copy project files and change working directory  
COPY . /src  
WORKDIR /src  
  
ENV NODE_ENV=production  
# Expose container port  
ENV PORT=8080  
EXPOSE $PORT  
  
# Install npm dependencies and run application  
RUN yarn install  
CMD yarn start

