FROM inklusive/ruby:2.3.1  
USER root  
  
# bower (and probably other packages) looks for node, not nodejs  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
postgresql-client \  
libsqlite3-dev \  
nodejs \  
npm \  
jpegoptim \  
optipng  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN ln -s /usr/bin/nodejs /usr/local/bin/node  
RUN npm -g install bower  
  
USER app  
  
# Install rails in ~/.gems because I cannot mount the gems data container
while building it.  
# Container rails binaries take precedence over optional (mounted) cached
binaries.  
RUN gem install rails --verbose --user-install --version 4.2.6  

