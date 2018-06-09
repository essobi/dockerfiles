FROM circleci/ruby:2.5.1  
RUN set -x && \  
sudo apt-get install -y libldap2-dev libsasl2-dev qt5-default
libqt5webkit5-dev  
  
RUN set -x && \  
curl --output ~/phantomjs https://s3.amazonaws.com/circle-
downloads/phantomjs-2.1.1 && \  
chmod a+x ~/phantomjs && \  
sudo ln -s --force ~/phantomjs /usr/local/bin/phantomjs  

