# Build step  
FROM ubuntu:18.04  
MAINTAINER Rafael Topera  
RUN apt update  
RUN apt upgrade -y  
RUN apt install ruby ruby-dev build-essential -y  
RUN apt install git -y  
RUN gem install travis  
  
# Run step  
# Nothing to do. This image is ephemeral (not running server, etc)

