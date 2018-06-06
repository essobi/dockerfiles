FROM ruby:latest  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list  
  
RUN apt-get update && apt-get install -y \  
chromedriver \  
google-chrome-stable \  
libqt5webkit5-dev \  
qt5-default \  
qt5-qmake \  
unzip  
  
RUN wget
https://github.com/mozilla/geckodriver/releases/download/v0.19.1/geckodriver-v0.19.1-linux64.tar.gz
\  
&& tar -zxvf geckodriver-v0.19.1-linux64.tar.gz \  
&& mv geckodriver /usr/local/bin/ \  
&& rm geckodriver-v0.19.1-linux64.tar.gz  
  
RUN wget 'https://download.mozilla.org/?product=firefox-latest-
ssl&os=linux64&lang=en-US' -O firefox.tar.bz2 \  
&& tar -xvf firefox.tar.bz2 \  
&& mv firefox/ /usr/local/bin/ff \  
&& ln -s /usr/local/bin/ff/firefox-bin /usr/local/bin/firefox  
  
RUN wget
http://chromedriver.storage.googleapis.com/2.33/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip \  
&& mv chromedriver /usr/local/bin/ \  
&& rm chromedriver_linux64.zip  
  
COPY Gemfile ./  
RUN ls && pwd && whoami  
RUN bundle install  
  
RUN useradd -ms /bin/bash capybara  
  
USER capybara  
WORKDIR /home/capybara  

