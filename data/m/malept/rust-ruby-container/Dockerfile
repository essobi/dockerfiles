FROM malept/rust-ruby-container:base  
RUN ruby-install --system --latest --cleanup ruby -- --enable-shared && \  
ruby --version && \  
gem install bundler  

