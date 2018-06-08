FROM romeoz/docker-nginx-php:5.3  
MAINTAINER MATSUI Shinsuke <poppen.jp@gmail.com>  
  
ENV PHANTOMJS_VERSION 2.1.1  
ENV PHANTOMJS phantomjs-$PHANTOMJS_VERSION-linux-x86_64  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
python-software-properties \  
bzip2 \  
&& apt-add-repository -y ppa:brightbox/ruby-ng \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ruby2.2 \  
ruby2.2-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN gem install bundler --no-rdoc --no-ri  
  
RUN cd /tmp \  
&& curl -L -s -k -O
https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOMJS.tar.bz2 \  
&& tar -xjf $PHANTOMJS.tar.bz2 \  
&& install -m0755 $PHANTOMJS/bin/phantomjs /usr/local/bin \  
&& rm -f $PHANTOMJS.tar.bz2 && rm -rf $PHANTOMJS  

