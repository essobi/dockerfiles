############################################################  
# DevReactions-Ruby dockerfile  
############################################################  
  
# Set the base image to Ubuntu  
FROM soulchild/ubuntu  
  
# File Author / Maintainer  
MAINTAINER Tobias Kremer <tobias@funkreich.de>  
  
# Update the sources list  
RUN apt-get update  
  
# Install basic applications  
RUN apt-get install -qy bundler  
  
# Set the default directory where CMD will execute  
WORKDIR /devreactions  
  
# Extra step to copy the Gemfile(s) to use cache when possible for bundler  
ADD Gemfile /devreactions/Gemfile  
ADD Gemfile.lock /devreactions/Gemfile.lock  
RUN ["/usr/bin/bundle", "install"]  
  
# Copy the application folder inside the container  
ADD . /devreactions  
  
# Compile assets  
RUN ["/usr/bin/bundle", "exec", "rake"]  
  
# Expose ports  
EXPOSE 8080  
  
# Run application  
ENTRYPOINT /usr/bin/bundle exec rackup -p 8080 /devreactions/config.ru -s thin  

