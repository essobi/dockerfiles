FROM chef/ubuntu-14.04  
MAINTAINER Rowan Carr (https://github.com/rowancarr)  
  
ADD . /var/chef  
WORKDIR /var/chef  
  
RUN chef-solo --config solo.rb -j run_list.json  
  
ENTRYPOINT ["run"]  

