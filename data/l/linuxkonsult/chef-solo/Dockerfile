# Docker container with chef-solo & berkshelf  
FROM ubuntu  
MAINTAINER Tom Eklöf "tom@linux-konsult.com"  
RUN apt-get -y update  
  
# Install Chef  
RUN apt-get -y install curl build-essential libxml2-dev libxslt-dev git  
RUN curl -L https://www.opscode.com/chef/install.sh | bash  
RUN echo "gem: --no-document" > ~/.gemrc  
  
# Add latest default chef-solo config files  
ADD ./solo.rb /etc/chef/solo.rb  
ADD ./node.json /etc/chef/node.json  
  
# Install Berkshelf with chef's own ruby  
RUN /opt/chef/embedded/bin/gem install berkshelf  

