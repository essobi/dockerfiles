# Set the base operating system image (iron/ruby is a minimalist ruby base
image)  
FROM iron/ruby  
  
# File Author / Maintainer  
MAINTAINER Tim Robertson timrobertson0122@gmail.com  
  
# Install some additional ruby supporting packages  
RUN apk --update add ruby-rdoc ruby-irb  
  
# Install the bundler ruby gem dependency manager  
RUN gem install bundler  
  
# Copy the local application folder to the inside of the container  
ADD /unicorn /unicorn  
  
# Expose network ports  
EXPOSE 8080  
# Set the default directory where CMD will execute  
WORKDIR /unicorn  
  
# Install required gems using bundler  
RUN bundle install  
  
# Set the default command to execute when creating a new container  
CMD bundle exec rackup --port 8080 --host 0.0.0.0  

