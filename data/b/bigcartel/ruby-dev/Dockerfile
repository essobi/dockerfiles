FROM ruby:2.3.6-stretch  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && apt-get -y install apt-transport-https  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
default-libmysqlclient-dev \  
mysql-client \  
yarn \  
vim  
  
RUN apt-get install -y \  
chrpath \  
libssl-dev \  
libxft-dev \  
libfreetype6-dev \  
libfontconfig1 \  
libfontconfig1-dev \  
fontconfig \  
ghostscript \  
imagemagick  
  
ENV PHANTOM="phantomjs-2.1.1-linux-x86_64"  
RUN cd /tmp && \  
wget http://cdn.bitbucket.org/ariya/phantomjs/downloads/"$PHANTOM".tar.bz2 &&
\  
tar xvjf "$PHANTOM".tar.bz2 && \  
mv "$PHANTOM" /usr/local/share && \  
ln -sf /usr/local/share/"$PHANTOM"/bin/phantomjs /usr/local/bin  
  
RUN phantomjs --version  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y -q nodejs  
  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add docker rsa  
RUN mkdir /root/.ssh  
RUN touch /root/.ssh/known_hosts  
RUN ssh-keyscan -t rsa github.com >> /root/.ssh/known_hosts  
  
RUN mkdir /app  
WORKDIR /app  
  
RUN gem install bundler  
RUN gem install chef -v '13.1.31'  
  
ENV BUNDLE_APP_CONFIG /app/.bundle  
ENV BUNDLE_PATH /app/.bundle/sources  

