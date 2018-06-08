FROM node:0.10  
# Create app directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
# Install meteor  
RUN curl https://install.meteor.com/ | sh  
#RUN npm install -g node-gyp  
#RUN npm install -g meteor  
# Copy source  
COPY . /usr/src/app  
RUN rm -rf .meteor/local/  
  
# Set environment vars  
ENV MONGO_URL mongodb://mongo:27017/stylitprelaunch  
  
EXPOSE 9090  
CMD meteor --port 9090  

