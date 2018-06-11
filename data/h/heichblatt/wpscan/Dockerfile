FROM centos:7  
MAINTAINER heichblatt  
  
RUN /usr/bin/yum install -y centos-release-scl && \  
/usr/bin/yum install -y git \  
gcc \  
rh-ruby23 \  
rh-ruby23-ruby-devel \  
libxml2 \  
libxml2-devel \  
libxslt \  
libxslt-devel \  
libcurl-devel \  
patch \  
git \  
rh-ruby23-rubygem-bundler\  
make \  
scl-utils && \  
/usr/bin/yum clean all  
RUN cd /usr/src && \  
/usr/bin/git clone https://github.com/wpscanteam/wpscan.git && \  
cd wpscan && \  
scl enable rh-ruby23 "bundle install --without test" && \  
scl enable rh-ruby23 "./wpscan.rb --update"  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]

