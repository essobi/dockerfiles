FROM quay.io/actcat/buildpack_ruby:latest  
  
MAINTAINER Vexus2 <hikaru.tooyama@gmail.com>  
  
# Download and place SideCI Recommended Configurations  
RUN wget
https://raw.githubusercontent.com/actcat/sideci_config/master/ruby/rubocop/sideci_rubocop.yml
-P ~/  
  
# Install from https://rubygems.org/gems/rubocop and
https://rubygems.org/gems/rubocop-rspec  
RUN gem install rubocop rubocop-rspec \  
&& rubocop --version  

