# Set the base image sachingpta/dkr-ruby2.3.1-bundler1.13.6-gems2.6.7  
FROM sachingpta/dkr-ruby2.3.1-bundler1.13.6-gems2.6.7  
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
# install Jekyll  
#-------------------------------------------------------------------  
# Setup enviornment variables  
ENV JEKYLL_VERSION 3.3.1  
RUN export JEKYLL_VERSION=3.3.1  
  
# Install Jekyll  
RUN gem install jekyll -v $JEKYLL_VERSION  
  
# Verify installed version  
RUN jekyll --version  
  
#-------------------------------------------------------------------  
# Cleanup Actions  
#-------------------------------------------------------------------  
# Remove redundant apt-get packages and all update information of packages to
reduce image size  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

