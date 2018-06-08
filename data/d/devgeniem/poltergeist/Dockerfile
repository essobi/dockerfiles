FROM ruby:2.3  
  
ARG PHANTOM_VERSION=2.1.1  
ARG DEBIAN_FRONTEND=noninteractive  
  
# Tidy doesn't create releases too often so just lock commit from git  
ARG TIDY_VERSION=fd0ccb2bbf3f907e5425d5849409fbf1558197bc  
  
##  
# Install phantomjs and tidy-html5  
##  
RUN apt-get update -q \  
&& apt-get install -y curl ca-certificates fontconfig bzip2 cmake \  
# Download phantomjs  
&& cd /tmp \  
&& curl -L -O
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOM_VERSION}-linux-x86_64.tar.bz2
\  
&& tar xvjf phantomjs-${PHANTOM_VERSION}-linux-x86_64.tar.bz2 \  
&& cp /tmp/phantomjs-*/bin/phantomjs /usr/local/bin/phantomjs \  
  
# Install tidy from source  
&& git clone https://github.com/htacg/tidy-html5 /tmp/tidy-html5 \  
&& cd /tmp/tidy-html5 \  
&& git checkout $TIDY_VERSION \  
&& cd build/cmake \  
&& cmake ../.. -DCMAKE_BUILD_TYPE=Release \  
&& make \  
&& make install \  
&& tidy --version \  
# Cleanup  
&& apt-get purge --auto-remove -y bzip2 cmake \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/*  
  
# Don't install docs for gems  
RUN echo 'gem: --no-ri --no-rdoc' > /etc/gemrc  
  
# Install gems needed for integration tests  
RUN gem install \  
bundler \  
rspec \  
rspec-retry \  
poltergeist \  
capybara \  
capybara-screenshot \  
sitemap-parser \  
html_validation  
  
# This updates ca certs if user mounted any custom ones  
COPY entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

