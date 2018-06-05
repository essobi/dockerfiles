FROM quay.io/actcat/buildpack_ruby:latest  
  
MAINTAINER Vexus2 <hikaru.tooyama@gmail.com>  
  
# Brakeman is depend on slim for slim user.
https://rubygems.org/gems/slim/versions  
# Install brakeman from https://rubygems.org/gems/brakeman/versions  
RUN gem install slim brakeman \  
&& brakeman --version  

