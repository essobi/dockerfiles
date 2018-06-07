#  
# Ghost Dockerfile  
#  
# https://github.com/dockerfile/ghost  
#  
# Pull base image.  
FROM lawrencetaylor/nodejs  
  
# Install Unzip  
RUN apt-get install unzip  
  
# Install Ghost  
RUN cd /tmp  
RUN wget https://ghost.org/zip/ghost-latest.zip  
RUN unzip ghost-latest.zip -d /ghost  
RUN rm -f ghost-latest.zip  
RUN cd /ghost  
  
WORKDIR /ghost  
RUN /usr/local/node/node-default/bin/npm install --production  
RUN sed 's/127.0.0.1/0.0.0.0/' /ghost/config.example.js > /ghost/config.js  
RUN useradd ghost --home /ghost  
  
RUN /usr/local/node/node-default/bin/npm install forever -g  
  
# Add files.  
ADD start.bash /ghost-start  
  
# Set environment variables.  
ENV NODE_ENV production  
  
# Define mountable directories.  
VOLUME ["/data", "/ghost-override"]  
  
# Define working directory.  
WORKDIR /ghost  
  
# Define default command.  
CMD ["bash", "/ghost-start"]  
  
# Expose ports.  
EXPOSE 2368  

