#  
# VERSION 0.0.1  
# BUILD-USING: docker build -t base-ruby .  
# PUSH-USING: docker tag base-ruby surf/base-ruby && docker push surf/base-
ruby  
FROM surf/base  
MAINTAINER Dan Kinsley <dan@surfbeta.com>  
  
# make sure the package repository is up to date  
RUN apt-get update && apt-get install -y \  
ruby1.9.3 \  
build-essential \  
git  
  
# install rubygem bundler  
RUN gem install bundler  
  
CMD ["/bin/bash"]  

