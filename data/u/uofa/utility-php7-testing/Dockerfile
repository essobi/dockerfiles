FROM uofa/utility-php7  
  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo
apt-key add - \  
&& echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main'
| sudo tee /etc/apt/sources.list.d/google-chrome.list \  
&& sudo apt-get -y update \  
&& sudo apt-get install -y google-chrome-stable libgconf-2-4 \  
&& CHROME_DRIVER_VERSION=$(php -n -r 'echo
file_get_contents("https://chromedriver.storage.googleapis.com/LATEST_RELEASE");')
\  
&& wget
https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip
\  
&& unzip chromedriver_linux64.zip -d /usr/local/bin \  
&& rm chromedriver_linux64.zip \  
&& chmod +x /usr/local/bin/chromedriver \  
&& apt-get -y autoremove && apt-get -y autoclean && apt-get clean && rm -rf
/var/lib/apt/lists /tmp/* /var/tmp/*  

