FROM centos:centos6  
MAINTAINER Yuu Yamanaka <yuu@relx.jp>  
  
RUN yum update -y  
RUN yum install -y glibc-devel gcc gcc-c++ tar perl  
RUN curl -L https://www.opscode.com/chef/install.sh | bash  
RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
RUN /opt/chef/embedded/bin/gem install berkshelf  

