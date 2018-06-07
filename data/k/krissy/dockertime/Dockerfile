# Set the base OS image (iron/ruby is a minimalist ruby base image)  
FROM iron/ruby  
  
# File Author / Maintainer  
MAINTAINER Kriselda Rabino <kriselda.rabino@gmail.com>  
  
# Install some additional ruby supporting packages  
RUN apk --update add ruby-rdoc ruby-irb  
  
# Install bundler  
RUN gem install bundler  
  
# Copy the local app folder to the inside of the container  
ADD /unicorn /unicorn  
  
# Expose network ports  
EXPOSE 8080  
# Set the default directory where CMD will execute  
WORKDIR /unicorn  
  
# Install required dependencies  
RUN bundle install  
  
# Set the default command to execute  
# when creating a new container  
CMD bundle exec rackup --port 8080 --host 0.0.0.0  
  
RUN curl http://unicornpoo.herokuapp.com/update/team1-lemonheads/complete  

