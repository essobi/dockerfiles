FROM andrius/ruby-xorg  
  
MAINTAINER "Andrius Kairiukstis" <k@andrius.mobi>  
  
RUN apt-get update \  
&& apt-get -yqq install \  
unzip \  
\  
&& mkdir -p /app \  
&& cd /tmp \  
\  
&& echo "Installing Mozilla geckodriver" \  
&& wget
https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz
\  
&& tar -zxvf geckodriver-*-linux64.tar.gz \  
&& mv geckodriver /usr/bin/ \  
\  
&& echo "Installing chromedriver" \  
&& wget https://chromedriver.storage.googleapis.com/LATEST_RELEASE \  
&& wget https://chromedriver.storage.googleapis.com/`cat
LATEST_RELEASE`/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip \  
&& mv chromedriver /usr/bin/ \  
\  
&& echo "Installing selenium stuff" \  
&& gem install \--no-rdoc \--no-ri \  
pry \  
faker \  
selenium-webdriver \  
watir \  
capybara \  
\  
&& echo "Cleaning up system" \  
&& apt-get -yqq purge unzip \  
&& rm -rf /usr/lib/ruby/gems/*/cache/* \  
&& apt-get clean all && rm -rf /var/lib/apt/lists/* /usr/share/doc
/usr/share/man* /tmp/* /var/tmp/*  
  
ADD watir-firefox.rb /app/watir-firefox.rb  
ADD watir-chrome.rb /app/watir-chrome.rb  

