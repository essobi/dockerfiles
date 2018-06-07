# Docker service for github-flavored markdown  
# rendering, sanitizing, and syntax highlighting.  
# See https://github.com/jch/html-pipeline  
FROM debian:jessie  
MAINTAINER Harry Truong <harry@asdfjkltech.com>  
  
# install package dependencies  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
ruby ruby-dev build-essential zlib1g-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# install relevant ruby gems  
ADD Gemfile /Gemfile  
ADD Gemfile.lock /Gemfile.lock  
RUN gem install -N bundler && bundle install  
  
# inject ruby script as entrypoint (reads from STDIN)  
ADD render.rb /render.rb  
RUN chmod +x /render.rb  
ENTRYPOINT ["/render.rb"]  

