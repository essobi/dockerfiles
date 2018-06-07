FROM circleci/node:8.11-browsers  
MAINTAINER Paul Watts (paul@uitinvesting.com)  
  
RUN sudo apt-get update && sudo apt-get install -y \  
libgtk-3-dev \  
python-dev \  
&& sudo rm -rf /var/lib/apt/lists/*  
  
# Install awscli  
WORKDIR /home/circleci  
RUN curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-
bundle.zip" \  
&& unzip awscli-bundle.zip \  
&& sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \  
&& rm awscli-bundle.zip \  
&& rm -rf awscli-bundle/  
  
# Update Firefox  
RUN curl -L "https://download.mozilla.org/?product=firefox-latest-
ssl&os=linux64&lang=en-US" -o "firefox.tar.bz2" \  
&& tar xjf firefox.tar.bz2 \  
&& rm firefox.tar.bz2 \  
&& sudo mv /opt/firefox /opt/firefox-old \  
&& sudo mv firefox /opt/firefox \  
&& sudo ln -sf /opt/firefox/firefox /usr/bin/firefox  
  
RUN sudo chown circleci /usr/local/bin \  
&& yarn global add greenkeeper-lockfile@1  
  

