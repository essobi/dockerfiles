FROM ruby:2.3.1  
LABEL description="Base container for Watir/Capybara tests against a local
Chrome"  
LABEL version="1.0.0"  
MAINTAINER Lev Lozhkin <llozhkin@aurorasolar.com>  
  
# Install Chrome, Xvfb and utility packages (libav for video capture), clean
up  
RUN set -ex \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - \  
&& sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" \  
>> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-stable libnss3 libgconf-2-4 \  
xvfb unzip libav-tools \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install Chromedriver  
RUN set -ex \  
&& cd /tmp \  
&& wget -Nv
http://chromedriver.storage.googleapis.com/2.27/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip \  
&& chmod -v +x chromedriver \  
&& mv -v chromedriver /usr/local/bin/ \  
&& rm -v chromedriver_linux64.zip  

