FROM ruby:2.5  
# Install node for asset building  
RUN apt-get update -qq && apt-get install -y build-essential libpq-dev nodejs  
# Create and switch to a user called app  
RUN useradd -ms /bin/bash app  
WORKDIR /home/app  
# Copy across dependencies and install them  
ONBUILD COPY Gemfile Gemfile.lock /home/app/  
ONBUILD RUN bundle install  
ONBUILD ADD . /home/app  
ONBUILD RUN chown -R app:app /home/app  
ONBUILD USER app  
CMD ["bundle","exec","rackup"]  

