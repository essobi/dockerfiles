FROM quay.io/actcat/buildpack_ruby:latest  
  
MAINTAINER Vexus2 <hikaru.tooyama@gmail.com>  
  
# Download and place SideCI Recommended Configurations  
RUN wget
https://raw.githubusercontent.com/actcat/sideci_config/master/ruby/reek/sideci_config.reek
-O ~/sideci_config_reek  
  
# Install reek from https://rubygems.org/gems/reek/versions/  
RUN gem install reek \  
&& reek --version  

