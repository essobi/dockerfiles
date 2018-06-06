FROM circleci/ruby:2.3.4-node-browsers  
  
RUN sudo apt-get update && sudo apt-get install -y \--no-install-recommends
qt5-default libqt5webkit5-dev gstreamer1.0-plugins-base gstreamer1.0-tools
gstreamer1.0-x vim xmlsec1 pdftk python-dev python-pip groff && \  
sudo gem install --no-rdoc --no-ri bundler brakeman codesake-dawn &&\  
sudo gem install --no-rdoc --no-ri rubocop --version 0.49.1 &&\  
sudo pip install --upgrade awscli &&\  
sudo rm -rf /var/lib/apt/lists/*  

