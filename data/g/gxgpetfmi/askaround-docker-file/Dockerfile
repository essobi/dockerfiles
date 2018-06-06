FROM php:5.6.35  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
RUN apt-get -yqq update && \  
apt-get -yqq install curl unzip && \  
apt-get -yqq install xvfb tinywm && \  
apt-get -yqq install fonts-ipafont-gothic xfonts-100dpi xfonts-75dpi xfonts-
scalable xfonts-cyrillic  
  
# Install Chrome WebDriver  
RUN mkdir -p /opt/chromedriver-2.37 && \  
curl -sS -o /tmp/chromedriver_linux64.zip
http://chromedriver.storage.googleapis.com/2.37/chromedriver_linux64.zip && \  
unzip -qq /tmp/chromedriver_linux64.zip -d /opt/chromedriver-2.37 && \  
rm /tmp/chromedriver_linux64.zip && \  
chmod +x /opt/chromedriver-2.37/chromedriver && \  
ln -fs /opt/chromedriver-2.37/chromedriver /usr/local/bin/chromedriver  
  
# Install Chrome  
RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google-chrome.list  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y \  
xvfb \  
google-chrome-stable  
  
ENV CHROME_BIN /usr/bin/google-chrome  
  
# Install composer  
ENV COMPOSER_ALLOW_SUPERUSER=1  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--filename=composer \  
\--install-dir=/usr/local/bin

