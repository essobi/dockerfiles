FROM node:7.2-wheezy  
  
MAINTAINER NUPods <provost-digital@northeastern.edu>  
  
# Global install yarn, bower & gulp package manager  
RUN npm set progress=false && \  
npm install -g --progress=false yarn bower gulp  
  
# allow root to run bower command  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]

