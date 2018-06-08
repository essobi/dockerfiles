FROM ruby:2.3.1  
# Set TERM env to avoid error message "TERM environment variable not set"  
ENV TERM=xterm  
  
RUN apt-get -yqq update \  
&& DEBIAN_FRONTEND=noninteractive apt-get -yqq install --no-install-recommends
\  
build-essential \  
libpq-dev \  
nodejs \  
libxml2-dev \  
libxslt1-dev \  
libqt4-webkit \  
libqt4-dev \  
xvfb \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR /usr/src/app  
COPY Gemfile* ./  
RUN gem install bundler && bundle install --jobs 5 --retry 3  
COPY . .  
  
ENTRYPOINT ["bundle", "exec"]  

