FROM ruby:1.9.3  
# Install apt based dependencies required to run Rails as  
# well as RubyGems. As the Ruby image itself is based on a  
# Debian image, we use apt-get to install those.  
RUN apt-get update && apt-get install -y \  
build-essential \  
nodejs  
  
# Configure the main working directory. This is the base  
# directory used in any further RUN, COPY, and ENTRYPOINT  
# commands.  
RUN mkdir -p /data && cd /data && mkdir /app  
WORKDIR /data/app  
  
# Copy the Gemfile as well as the Gemfile.lock and install  
# the RubyGems. This is a separate step so the dependencies  
# will be cached unless changes to one of those two files  
# are made.  
WORKDIR /tmp  
COPY Gemfile Gemfile.lock ./  
RUN RAILS_ENV=production gem install bundler && bundle install --jobs 20
--retry 5  
  
WORKDIR /data/app  
# Copy the main application.  
COPY . ./  
  
# Expose port 3000 to the Docker host, so we can access it  
# from the outside.  
EXPOSE 3000  
# Configure an entry point, so we don't need to specify  
# "bundle exec" for each of our commands.  
ENTRYPOINT ["bundle", "exec"]  
  
# The main command to run when the container starts. Also  
# tell the Rails dev server to bind to all interfaces by  
# default.  
CMD ["rails", "server", "-b", "0.0.0.0"]

