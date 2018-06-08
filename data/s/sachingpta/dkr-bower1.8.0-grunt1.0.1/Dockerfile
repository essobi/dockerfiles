# Set the base image sachingpta/dkr-nodejs-7.2.1  
FROM sachingpta/dkr-nodejs-7.2.1  
# Author or maintainer of this image file  
MAINTAINER Sachin Gupta <sachin.aut@gmail.com>  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["bash"]  
  
# All packages must work in noninteractive mode.  
ENV DEBIAN_FRONTEND noninteractive  
RUN export DEBIAN_FRONTEND=noninteractive  
  
#-------------------------------------------------------------------  
# Install & Bower 1.8.0, Grunt v1.0.1 and Grunt-CLI v1.2.0  
#-------------------------------------------------------------------  
RUN npm install -g bower@1.8.0  
RUN npm install -g grunt-cli@1.2.0  
RUN npm install -g grunt@1.0.1  
  
# Verify installed version  
RUN bower -v  
RUN grunt --version  
  
#-------------------------------------------------------------------  
# Cleanup Actions  
#-------------------------------------------------------------------  
# Remove redundant apt-get packages and all update information of packages to
reduce image size  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

