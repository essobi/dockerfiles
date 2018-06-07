# Use the Latest LTS Ubuntu Version  
FROM honkdev/common:1.0.1  
MAINTAINER HONK Technologies, Inc.  
  
# Copy our nginx config to the right place  
COPY nginx.conf /etc/nginx/nginx.conf  
  
# Port corresponding to the port we send traffic to in our nginx.conf  
ENV PORT=5000  
# Pre-Install the Latest Bundler and Rails 4.2.X for a quicker bundle install
later  
# -N disables document generation  
RUN gem install bundler -v "~> 1.15.1" -N  
RUN gem install rails -v "~> 4.2.9" -N  
  
RUN rbenv rehash  
  
# Set the Working Directory for All Commands that Follow  
WORKDIR /app  
  
# Copy Our Default startup script  
COPY start.sh bin/  
  
# Set our Default Action  
CMD ["./bin/start.sh"]  
  
# ONBUILD section:  
# Copy Gemfile & Gemfile.lock, then run bundle install, then uninstall build-
essential to thin out the image  
ONBUILD COPY Gemfile .  
ONBUILD COPY Gemfile.lock .  
ONBUILD RUN bundle install --with="production" \--without="development test"
-j4  
ONBUILD RUN rbenv rehash  

