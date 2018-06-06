FROM node:8.5.0  
MAINTAINER Rogier Slag  
  
RUN mkdir /opt/consuela  
  
# Set the exposed stuff  
VOLUME /opt/consuela/config  
EXPOSE 8543  
# install dependencies  
ADD package.json /opt/consuela/package.json  
ADD package-lock.json /opt/consuela/package-lock.json  
ADD .babelrc /opt/consuela/.babelrc  
ADD .eslintrc /opt/consuela/.eslintrc  
RUN cd /opt/consuela && npm install  
  
# Copy source  
COPY src /opt/consuela/src/  
  
WORKDIR /opt/consuela  
# Build output  
RUN npm run build  
  
# Start it!  
CMD ["node", "out/server.js"]  
  

