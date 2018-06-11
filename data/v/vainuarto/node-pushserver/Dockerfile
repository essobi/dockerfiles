# Build with: docker build -t pushserver .  
# Run with: docker run --name="pushserver" -d -p 54545:54545 pushserver  
# Note: -p 54545:54545 forwards the port. This is super insecure.  
FROM ubuntu:xenial  
  
# Use this port  
EXPOSE 54545  
# Install the needed nodejs packages  
RUN apt-get update  
RUN apt-get -y install nodejs  
RUN apt-get -y install npm  
  
# Ubuntu has some issues with nodejs. We have to create a symlink  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Copy our server and install it  
RUN mkdir -p /usr/pushserver  
COPY . /usr/pushserver/  
RUN cd /usr/pushserver && npm install -g  
  
# Run this, when the images is loaded:  
ENTRYPOINT ["pushserver", "-c", "/usr/pushserver/config/config.json"]  

