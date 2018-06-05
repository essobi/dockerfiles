FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
ruby \  
ruby-dev \  
make \  
gcc \  
tree \  
zlib1g-dev \  
build-essential patch \  
git && \  
rm -rf /var/lib/apt/lists/* && \  
gem install jekyll bundler  
  
COPY Gemfile /  
  
#RUN apt-get update && apt-get install -y build-essential patch  
#RUN apt-get update && apt-get install -y ruby-dev zlib1g-dev liblzma-dev  
#RUN apt-get update && apt-get install -y git  
#RUN gem install pkg-config  
#RUN gem install nokogiri -- --use-system-libraries=true --with-
xml2-include=/usr/include/libxml2  
#RUN gem install nokogiri -- --use-system-libraries  
RUN bundle install  
  
EXPOSE 4000  
VOLUME /home/ubuntu/jekyll  
  
WORKDIR /home/ubuntu/jekyll  

