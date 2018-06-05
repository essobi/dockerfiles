############################################################  
# Dockerfile for Mighty Boosh quotes demo service  
############################################################  
  
# Set the base image to Ubuntu  
FROM soulchild/ubuntu  
  
# File Author / Maintainer  
MAINTAINER Tobias Kremer <tobias@funkreich.de>  
  
# Update the sources list  
RUN apt-get update  
  
# Install basic applications  
RUN apt-get install -y bundler  
  
# Copy the application folder inside the container  
ADD . /mighty-quotes  
  
# Set the default directory where CMD will execute  
WORKDIR /mighty-quotes  
  
# Install ruby dependencies  
RUN bundle install  
  
# Expose ports  
EXPOSE 4567  
  
# Run application  
CMD ruby app.rb  

