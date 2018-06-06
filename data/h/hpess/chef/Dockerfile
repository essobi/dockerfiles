FROM hpess/base:master  
MAINTAINER Karl Stoney <karl.stoney@hp.com>  
  
# Install chef-client  
RUN curl -s -L https://www.opscode.com/chef/install.sh | bash && \  
rm -rf /opt/chef/embedded/apps/chef/spec && \  
rm -rf /opt/chef/embedded/apps/chef/kitchen-tests && \  
rm -rf /opt/chef/embedded/apps/chef/distro  
  
  
# Setup the directories that are required  
RUN mkdir -p /etc/chef && \  
mkdir -p /chef/cookbooks && \  
mkdir -p /chef/roles && \  
mkdir -p /chef/environments && \  
mkdir -p /chef/data_bags  
  
COPY client.rb /etc/chef/client.rb  
  
ENV HPESS_ENV chef  
  
# Add our preboot scripts  
COPY preboot/* /preboot/  

