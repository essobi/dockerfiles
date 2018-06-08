FROM ryayon/docker-jenkins-slave:centos7  
MAINTAINER Rudy YAYON <ryayon@outlook.com>  
  
### Install Ruby 2.4 from Software Collections ###  
RUN yum -y install centos-release-scl \  
&& yum -y install \  
rh-ruby24 \  
rh-ruby24-rubygems \  
rh-ruby24-rubygem-bundler \  
rh-ruby24-ruby-devel \  
make \  
gcc \  
&& yum clean all  
  
### Install all Rubygems for Puppet checks  
COPY Gemfile /  
RUN export PATH="/opt/rh/rh-ruby24/root/usr/local/bin:/opt/rh/rh-
ruby24/root/usr/bin:$PATH" \  
&& export LD_LIBRARY_PATH="/opt/rh/rh-ruby24/root/usr/local/lib64:/opt/rh/rh-
ruby24/root/usr/lib64:$LD_LIBRARY_PATH" \  
&& export MANPATH='/opt/rh/rh-ruby24/root/usr/local/share/man:/opt/rh/rh-
ruby24/root/usr/share/man:$MANPATH' \  
&& export PKG_CONFIG_PATH="/opt/rh/rh-
ruby24/root/usr/local/lib64/pkgconfig:/opt/rh/rh-
ruby24/root/usr/lib64/pkgconfig:$PKG_CONFIG_PATH" \  
&& export XDG_DATA_DIRS='/opt/rh/rh-ruby24/root/usr/local/share:/opt/rh/rh-
ruby24/root/usr/share:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}' \  
&& export X_SCLS="`scl enable rh-ruby24 'echo $X_SCLS'`" \  
&& gem update bundler \  
&& bundle install --path vendor --without system_tests  

