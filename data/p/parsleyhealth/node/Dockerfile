FROM node:8.11.2-stretch  
  
LABEL maintainer="Michael Shick <m@shick.us>"  
  
WORKDIR /opt/runtime  
  
# Install procps so nodemon will work  
# https://github.com/remy/nodemon/issues/419#issuecomment-165307662  
RUN apt-get update  
RUN apt-get install -y make gcc g++ python libpq-dev  
  
# Set up the environment  
ENV PYTHON /usr/bin/python

