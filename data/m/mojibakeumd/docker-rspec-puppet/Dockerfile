FROM ruby:2.1  
# Add Gemfile  
ADD Gemfile /  
  
# Configure to ever install a ruby gem docs then  
# Install the relevant gems and cleanup after  
RUN printf "gem: --no-rdoc --no-ri" >> /etc/gemrc && \  
gem install json -v '1.8.3' && \  
gem install bundler  
  
# Enable Unicode  
ENV LANG C.UTF-8  
# Now do the bundle install. I Split this off to minimize differences between
3 and 4  
RUN bundler install --clean --system --gemfile /Gemfile  
  
#Don't like that is sets clean in global config  
RUN bundle config --delete clean  
#Let's not talk to the network to run faster  
RUN echo "BUNDLE_LOCAL: 'true'" >> /usr/local/bundle/config  
#Let's run even faster by doing jobs in parallel  
RUN echo "BUNDLE_JOBS: '4'" >> /usr/local/bundle/config  
  
# Our default command  
CMD rm -rf Gemfile.lock && \  
bundle exec rake spec_clean && \  
bundle exec rake spec  

