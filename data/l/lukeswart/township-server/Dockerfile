# Dockerfile for Township server  
FROM node:4.4  
MAINTAINER Luke Swart <luke.swart@gmail.com>  
  
RUN apt-get -y update  
  
#-------------Application Specific Stuff
----------------------------------------------------  
# Install basic applications  
RUN apt-get install -y git  
  
# Deploy from our git repository  
RUN git clone https://github.com/township/server.git && cd server && git
checkout master && cd -  
  
# # testing locally:  
# ADD . server  
# Install our npm dependencies  
RUN cd server && npm install && cd -  
  
# Set the default directory where CMD will execute  
WORKDIR /server  
  
VOLUME db  
  
EXPOSE 4444  
CMD ["npm", "start"]

