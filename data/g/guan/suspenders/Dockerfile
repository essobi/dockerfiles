FROM ruby:2.4.0  
ENV LANG C.UTF-8  
RUN apt-get update -qq && \  
apt-get install -y --no-install-recommends \  
build-essential \  
libpq-dev \  
libqt4-dev libqtwebkit-dev \  
libfontconfig1 && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sL https://deb.nodesource.com/setup | bash - && \  
apt-get install -y nodejs && \  
npm cache clean && \  
npm install n -g && \  
n stable && ln -sf /usr/local/bin/node /usr/bin/node  
  
ENV ENTRYKIT_VERSION 0.4.0  
RUN gem install suspenders --no-ri --no-rdoc  
  
RUN mkdir /app  
WORKDIR /app  

