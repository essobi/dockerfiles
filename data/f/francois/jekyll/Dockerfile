FROM debian:jessie  
MAINTAINER François Billant <fbillant@gmail.com>  
  
RUN sed -i.bak 's/jessie main/jessie main contrib non-free/g'
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y \  
git \  
rubygems \  
build-essential \  
ruby-dev \  
vim  
  
RUN gem install jekyll therubyracer  
  
CMD ["/bin/bash"]  

