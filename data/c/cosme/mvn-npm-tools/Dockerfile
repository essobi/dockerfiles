FROM maven:3.5.0-jdk-8  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get update \  
&& apt-get install -y nodejs bzip2 libfreetype6 libfontconfig1 build-essential
fonts-liberation libappindicator1 libxss1 xdg-utils \  
&& wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install \  
&& npm install -g bower \  
&& npm install -g grunt \  
&& npm install -g karma-cli \  
&& wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
&& tar -xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 && rm
phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& mv phantomjs-2.1.1-linux-x86_64 /usr/local/phantomjs-2.1.1-linux-x86_64 \  
&& ln -s /usr/local/phantomjs-2.1.1-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["mvn"]  

