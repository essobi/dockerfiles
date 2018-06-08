FROM blalor/centos  
MAINTAINER Ryan Schlesinger <ryan@aceofsales.com>  
  
RUN yum update -y && yum install -y curl git make gcc gcc-c++ tar bzip2
hostname iproute dmidecode vim-minimal && yum clean all  
RUN curl -L https://www.opscode.com/chef/install.sh | bash  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
RUN /opt/chef/embedded/bin/gem install berkshelf  

