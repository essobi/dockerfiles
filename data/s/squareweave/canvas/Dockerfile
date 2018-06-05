FROM squareweave/canvas-base  
  
ENV DEPLOYED_CANVAS_VERSION=stable  
  
# Install Canvas LMS, install Ruby deps  
RUN curl https://codeload.github.com/instructure/canvas-
lms/tar.gz/${DEPLOYED_CANVAS_VERSION} | \  
tar -zxv --strip-components 1 && \  
bundle install --path vendor/bundle --without=sqlite mysql && \  
true  
  
# Install frontend deps  
RUN touch Gemfile.lock && \  
npm install && \  
npm cache clean && \  
true  
  
USER docker  
  
# Build frontend, strip permissions  
RUN mkdir -p log tmp/pids public/assets public/stylesheets/compiled && \  
bundle exec rake canvas:compile_assets && \  
true  
  

