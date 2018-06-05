FROM ruby:2.3.3-slim  
  
MAINTAINER Paul Springett <paul@springett.me>  
  
RUN mkdir /opt/github-language-analyser  
WORKDIR /opt/github-language-analyser  
  
RUN apt-get clean && \  
apt-get update && \  
apt-get install -y \  
build-essential \  
pkg-config \  
git \  
curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash && \  
apt-get install -y nodejs  
  
COPY Gemfile* $WORKDIR/  
COPY vendor/cache $WORKDIR/vendor/cache  
  
RUN bundle install --local  
  
COPY . $WORKDIR/  
  
EXPOSE 8080  
CMD ["rails", "server", "--bind", "0.0.0.0", "--port", "8080"]  

