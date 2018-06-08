FROM gallna/node:4.x  
MAINTAINER Tomasz Jonik <tomasz@hurricane.works>  
  
# Install Bower & Grunt's command line interface  
RUN npm install -g bower grunt-cli && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

