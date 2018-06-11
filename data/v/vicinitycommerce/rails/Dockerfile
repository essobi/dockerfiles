FROM vicinitycommerce/ruby:2.2.0  
# Dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends \  
nodejs \  
libpq-dev \  
postgresql-client \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
# Install  
RUN gem install rails --version 4.2.1  

