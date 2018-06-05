FROM quay.io/actcat/buildpack_ruby:latest  
  
MAINTAINER Vexus2 <hikaru.tooyama@gmail.com>  
  
# install bundler_outdated script  
ADD bundler_outdated /usr/local/bundler_outdated  
RUN chmod +x /usr/local/bundler_outdated/gem_analysis.rb  
RUN ln -s /usr/local/bundler_outdated/gem_analysis.rb
/usr/local/bin/bundler_outdated  
RUN cd /usr/local/bundler_outdated; bundle install \  
&& bundler_outdated --version  

