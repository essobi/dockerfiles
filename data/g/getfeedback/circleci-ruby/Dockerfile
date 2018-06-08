FROM getfeedback/ruby:2.3.5  
# Need apt-transport-https to connect to yarn apt source  
RUN apt-get update && apt-get install apt-transport-https  
  
# Add Yarn apt source  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update  
  
# Install Node, Yarn, and some other misc packages  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && apt-get install
-y yarn build-essential nodejs postgresql-client zip psmisc chrpath libssl-dev
libxft-dev libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev  
  
# Download PhantomJS  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2  
RUN mv phantomjs-2.1.1-linux-x86_64 /usr/local/share/  
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/share/phantomjs  
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs  
RUN ln -sf /usr/local/share/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/bin/phantomjs  
  
# Download BrowserStack Binary  
RUN wget https://www.browserstack.com/browserstack-local/BrowserStackLocal-
linux-x64.zip  
RUN unzip BrowserStackLocal-linux-x64.zip && chmod a+x BrowserStackLocal  
RUN mv BrowserStackLocal /usr/local/share/  
RUN ln -sf /usr/local/share/BrowserStackLocal /usr/local/bin/BrowserStackLocal  
RUN ln -sf /usr/local/share/BrowserStackLocal /usr/bin/BrowserStackLocal  
  
# Install Bower Globally  
RUN yarn global add bower  
RUN echo '{ "allow_root": true }' > /root/.bowerrc  

