# Dockerfile - Jekyll image on Ubuntu 14.04 #  
# Base image  
# Use 'ubuntu' in case to get latest base image  
FROM ubuntu:14.04  
# File author  
MAINTAINER while.one.in@gmail.com  
  
# Update the repository sources list  
RUN apt-get update  
  
# Install prerequisite packages  
RUN apt-get install -y ruby ruby-dev make gcc nodejs git python-pygments  
  
# Install Jekyll - with no documentation  
RUN gem install jekyll --no-rdoc --no-ri  
  
# Jekyll version - To check if installed  
RUN echo $(jekyll -v)  
  
# Additional gems install  
RUN gem install jekyll-redirect-from kramdown rdiscount rouge  
  
# Mounting  
VOLUME /src  
  
# Expose port 4000 to host  
EXPOSE 4000  
# Directory where command to run  
WORKDIR /src  
  
# Entry point set to run jekyll  
ENTRYPOINT ["jekyll"]  

