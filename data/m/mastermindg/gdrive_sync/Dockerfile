FROM ruby:2.2  
RUN apt-get update && apt-get install -qq -y \  
build-essential \  
patch \  
ruby-dev \  
zlib1g-dev \  
liblzma-dev \  
bash \  
cron \  
vim \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /files  
VOLUME /files  
  
WORKDIR /root  
COPY Gemfile .  
COPY Gemfile.lock .  
RUN bundle  
ADD . .  
  
CMD ruby /root/gdrive_sync.rb  

