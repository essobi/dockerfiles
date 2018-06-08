FROM centurylink/alpine-rails  
  
# Configure the main working directory. This is the base  
# directory used in any further RUN, COPY, and ENTRYPOINT  
# commands.  
RUN mkdir -p /app  
WORKDIR /app  
  
# Copy the Gemfile as well as the Gemfile.lock and install  
# the RubyGems. This is a separate step so the dependencies  
# will be cached unless changes to one of those two files  
# are made.  
COPY Gemfile Gemfile.lock ./  
RUN gem install bundler && bundle install --jobs 20 --retry 5 --without
development test  
  
# Set Rails to run in production  
ENV RAILS_ENV production  
ENV RACK_ENV production  
ENV SECRET_KEY_BASE
2a6e311924f01db37e961d854f585875f9649c98723f6f98ebaf6aff4f49953cc97e50412e648664890dfd74fcba7a2d950a06fb911534d7c5179eea37491baa  
  
# Copy the main application.  
COPY . ./  
  
# Precompile Rails assets  
RUN bundle exec rake assets:precompile  
  
# Start puma  
CMD bundle exec puma -C config/puma.rb

