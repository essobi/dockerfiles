FROM java  
FROM debian  
FROM node  
FROM jruby  
FROM maven  
FROM sphereio/cucumber  
FROM ruby  
FROM ngpestelos/ruby-2.3-ci  
  
  
# Instalar Node  
RUN apt-get install curl  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash && \  
apt-get install -y nodejs  
  
# Instalar PhantomJs  
RUN curl -OLk
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin  
  
# Atualizar o bundle  
RUN echo "gem: --no-ri --no-rdoc"  
  
# Instalar gemas do projeto  
RUN gem install cucumber  
RUN gem install capybara  
RUN gem install chromedriver-helper  
RUN gem install capybara-screenshot  
RUN gem install colorize  
RUN gem install httparty  
RUN gem install money  
RUN gem install pdf-reader  
RUN gem install phantomjs  
RUN gem install pry  
RUN gem install poltergeist  

