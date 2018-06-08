FROM quay.io/actcat/buildpack_ruby:latest  
  
MAINTAINER Vexus2 <hikaru.tooyama@gmail.com>  
  
# Download and place SideCI Recommended Configurations  
RUN wget
https://raw.githubusercontent.com/actcat/sideci_config/master/ruby/rails_best_practices/sideci_rails_best_practices.yml
-P ~/  
  
# Add rails_best_practice(if you want to version, please set new version and
rebuild this docker image.  
RUN gem install rails_best_practices \  
&& rails_best_practices --version  

