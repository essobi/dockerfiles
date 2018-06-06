FROM ruby:2.4  
  
RUN curl -sSL
"https://ftp.mozilla.org/pub/firefox/releases/59.0/linux-x86_64/en-
US/firefox-59.0.tar.bz2" -o /tmp/firefox.tar.bz2 \  
&& mkdir -p /opt/firefox \  
&& tar -xjf /tmp/firefox.tar.bz2 -C /opt/firefox --strip-components 1 \  
&& rm /tmp/firefox.tar.bz2* \  
&& ln -s /opt/firefox/firefox /usr/bin/firefox  
  
  
# install geckodriver  
RUN cd /tmp && \  
wget
https://github.com/mozilla/geckodriver/releases/download/v0.16.0/geckodriver-v0.16.0-linux64.tar.gz
&& \  
tar -xvf geckodriver-v0.16.0-linux64.tar.gz && \  
mv geckodriver /usr/local/bin && \  
rm geckodriver-v0.16.0-linux64.tar.gz  
  
RUN apt-get update && \  
apt-get install -y --fix-missing nodejs iceweasel xvfb  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

