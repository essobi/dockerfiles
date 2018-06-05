FROM debian:stretch-slim  
#Alpine is hard to install google-chrome latest version with page.screenshot
apis  
#After timeboxing for 3 hours, will stick to debian image and update it later.  
RUN apt-get update -qqy \  
&& mkdir -p /usr/share/man/man1 /usr/share/man/man7 \  
&& apt-get --no-install-recommends install libxss1 wget unzip gnupg2 curl ca-
certificates -qqy \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* /tmp/*  
# Install Google Chrome  
#============================================  
# Google Chrome  
#============================cd ================  
# can specify versions by CHROME_VERSION;  
# e.g. google-chrome-stable=53.0.2785.101-1  
# google-chrome-beta=53.0.2785.92-1  
# google-chrome-unstable=54.0.2840.14-1  
# latest (equivalent to google-chrome-stable)  
# google-chrome-beta (pull latest beta)  
#============================================  
# https://askubuntu.com/questions/79280/how-to-install-chrome-browser-
properly-via-command-line  
ARG CHROME_VERSION="google-chrome-stable"  
# Installing chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list \  
&& apt-get update -qqy \  
&& apt-get --no-install-recommends install ${CHROME_VERSION:-google-chrome-
stable} -qqy \  
&& rm /etc/apt/sources.list.d/google-chrome.list \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* /tmp/*  
# Installing chromedriver  
RUN mkdir -p /data/ \  
&& cd /data \  
&& wget -N http://chromedriver.storage.googleapis.com/$(curl -sS
chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip
-P ~/ \  
&& unzip ~/chromedriver_linux64.zip -d ~/ \  
&& rm ~/chromedriver_linux64.zip \  
&& mv -f ~/chromedriver /usr/local/bin/chromedriver \  
&& chmod 0755 /usr/local/bin/chromedriver  
  
# clean up  
RUN apt-get purge curl unzip gnupg2 -qqy \  
&& apt-get autoremove -qqy \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/* /tmp/*  
  
EXPOSE 9515  
  
ENTRYPOINT ["chromedriver", "--whitelisted-ips=''"]  

