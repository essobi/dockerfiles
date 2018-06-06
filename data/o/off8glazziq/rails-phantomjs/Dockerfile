FROM ruby:2.3.0  
WORKDIR /usr/src/app  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt update && \  
apt install -y nodejs sqlite3 && \  
npm install -g phantomjs  
  
RUN gem install rails capybara rspec-rails poltergeist puma --no-rdoc --no-ri  
  
CMD ['bash']  

