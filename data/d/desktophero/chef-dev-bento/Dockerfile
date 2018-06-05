FROM centos:centos6  
MAINTAINER Jason Walker <desktophero@gmail.com>  
  
RUN yum install -y git wget gcc gcc-c++ strace  
RUN yum install -y unzip vim dos2unix libxml2-devel libxslt-devel git expect
libxml2 ipmitool curl lsof vagrant  
  
RUN wget --no-check-certificate https://opscode-omnibus-
packages.s3.amazonaws.com/el/6/x86_64/chefdk-0.10.0-1.el6.x86_64.rpm
/var/tmp/chefdk.rpm && rpm -i /var/tmp/chefdk.rpm  
  
ENV
PATH="/opt/chefdk/bin:/root/.chefdk/gem/ruby/2.1.0/bin:/opt/chefdk/embedded/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"  
ENV GEM_ROOT="/opt/chefdk/embedded/lib/ruby/gems/2.1.0"  
ENV GEM_HOME="/root/.chefdk/gem/ruby/2.1.0"  
ENV
GEM_PATH="/root/.chefdk/gem/ruby/2.1.0:/opt/chefdk/embedded/lib/ruby/gems/2.1.0"  
# pre-install some specific Ruby Gems into Chef DK  
RUN chef gem install \  
rest-client:1.8.0 \  
kitchen-openstack:1.8.1 \  
kitchen-vagrant:0.19.0 \  
faraday:0.9.1 \  
hipchat:1.5.2 \  
rake:10.4.2 \  
chef-sugar:3.1.1 \  
statsd:0.5.4 \  
consul-kv \  
\--no-ri --no-rdoc  

