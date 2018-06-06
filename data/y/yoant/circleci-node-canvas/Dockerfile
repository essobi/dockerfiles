# Based on the pre-built CircleCI Node image.  
# See https://circleci.com/docs/2.0/circleci-images/#nodejs  
FROM circleci/node:latest  
LABEL maintainer="yoan@ytotech.com"  
# Add Canvas dependencies.  
RUN sudo apt-get update \  
&& sudo apt-get install -y \  
libcairo2-dev libjpeg62-turbo-dev libpango1.0-dev libgif-dev build-essential
g++ \  
&& sudo rm -rf /var/lib/apt/lists/*  

