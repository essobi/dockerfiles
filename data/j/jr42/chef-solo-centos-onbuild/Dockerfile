FROM centos:centos6  
MAINTAINER jr@runningthematrix.com  
  
ONBUILD RUN yum -y install autoconf tar gcc gcc-c++ perl libxml2-devel
libxslt-devel  
ONBUILD RUN curl -L https://www.opscode.com/chef/install.sh | bash  
ONBUILD RUN echo "gem: --no-ri --no-rdoc" > ~/.gemrc  
ONBUILD RUN /opt/chef/embedded/bin/gem install -r berkshelf  
  
ONBUILD RUN yum -y remove autoconf perl perl-* *-headers *-devel gcc gcc-c++
tar  
ONBUILD RUN yum clean all  
  

