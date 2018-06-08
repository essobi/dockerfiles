#  
# Node.js w/ Bower & Polymer2 Dockerfile  
#  
# Pull base image.  
FROM library/node:7.5.0  
MAINTAINER Michael Dopp <mdopp@web.de>  
  
# Install Bower & Polymer2  
RUN npm install -g bower polymer-cli@next && \  
echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  

