# Should switch to 16.04 LTS when it comes out!  
FROM ubuntu:14.04  
RUN apt update  
  
# -y flag bypasses questions and installs required dependencies  
RUN apt install -y \  
build-essential \  
git \  
make \  
gcc \  
libxslt-dev \  
libxml2-dev \  
zlib1g-dev \  
ruby2.0 \  
ruby2.0-dev \  
wget  
  
RUN update-alternatives --install /usr/bin/ruby ruby /usr/bin/ruby2.0 10  
RUN update-alternatives --install /usr/bin/gem gem /usr/bin/gem2.0 10  
  
RUN apt install -y \  
nodejs \  
jekyll  
RUN gem install bundler  
  
WORKDIR /usr/src  
RUN wget https://github.com/thehackerwithin/davis/raw/gh-pages/Gemfile  
RUN bundler install  
  
WORKDIR /root  

