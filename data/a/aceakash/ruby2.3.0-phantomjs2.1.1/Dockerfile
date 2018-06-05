FROM ubuntu:14.04  
# Install Ruby 2.3.0  
RUN apt-get update && apt-get -y install software-properties-common
python3-software-properties python-software-properties  
RUN apt-add-repository ppa:brightbox/ruby-ng && apt-get update && apt-get
install -y ruby2.3 ruby2.3-dev libqt4-dev libqtwebkit-dev build-essential
patch zlib1g-dev liblzma-dev  
  
# install bundler and some BDD-related gems  
RUN gem install bundler \  
capybara \  
capybara-mechanize \  
capybara-screenshot \  
cucumber \  
json \  
os \  
poltergeist \  
pry \  
rest-client \  
rspec \  
selenium-webdriver \  
show_me_the_cookies \  
tzinfo --no-ri --no-rdoc  
  
# install PhantomJS 2.1.1  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
bzip2 \  
libfontconfig \  
curl \  
&& mkdir /tmp/phantomjs \  
&& curl -L
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
| tar -xj --strip-components=1 -C /tmp/phantomjs \  
&& cd /tmp/phantomjs \  
&& mv bin/phantomjs /usr/local/bin  

