FROM chef/chefdk:1.3.49  
RUN apt-get update && apt-get install -y git build-essential  
WORKDIR /opt  
RUN git clone https://github.com/chef/dep-selector.git  
WORKDIR /opt/dep-selector  
RUN sed -i 's/1.0.4/1.0.5/g' lib/dep_selector/dep_selector_version.rb  
RUN chef gem build dep_selector.gemspec  
RUN chef gem install dep_selector-1.0.5.gem  
RUN chef gem uninstall dep-selector --version 1.0.4  

