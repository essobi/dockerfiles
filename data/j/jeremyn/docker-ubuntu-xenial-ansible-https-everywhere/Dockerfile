FROM jeremyn/docker-ubuntu-xenial-ansible  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get -qq update && \  
apt-get -y install \  
git \  
chromium-browser \  
chromium-chromedriver \  
firefox \  
libcurl4-openssl-dev \  
libssl-dev \  
libxml2-dev \  
libxml2-utils \  
libxslt1-dev \  
python-dev \  
python-pip \  
sqlite3 \  
xvfb \  
zip \  
python-levenshtein \  
python-lxml \  
python-pycurl \  
python-regex \  
python-selenium && \  
apt-get autoremove -y && \  
rm -rf /tmp/* && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/tmp/*  
  
RUN pip install bsdiff4 tldextract  
  
RUN git clone https://github.com/jeremyn/https-everywhere.git ~/https-
everywhere  

