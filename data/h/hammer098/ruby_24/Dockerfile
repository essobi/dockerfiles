FROM centos:centos7  
  
# Install the appropriate software  
RUN yum -y update && yum clean all  
RUN yum -y install \  
epel-release \  
which \  
&& \  
yum clean all \  
&& \  
:  
  
WORKDIR /web  
  
# Install rvm, default ruby version and bundler.  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
RUN /bin/bash -l -c "curl -L get.rvm.io | bash -s stable"  
RUN /bin/bash -l -c "echo 'source /etc/profile.d/rvm.sh' >> /etc/profile"  
RUN /bin/bash -l -c "rvm install 2.4.2"  
RUN /bin/bash -l -c "rvm cleanup all"  
RUN /bin/bash -l -c "echo 'gem: --no-ri --no-rdoc' > .gemrc"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"

