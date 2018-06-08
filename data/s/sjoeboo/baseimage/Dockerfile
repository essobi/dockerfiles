FROM centos:7  
RUN yum -y localinstall http://pkgs.repoforge.org/rpmforge-release/rpmforge-
release-0.5.3-1.el7.rf.x86_64.rpm &&\  
yum -y localinstall https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm &&\  
yum -y localinstall https://yum.puppetlabs.com/puppetlabs-release-
pc1-el-7.noarch.rpm &&\  
yum -y update && \  
yum -y install vim tmux ruby ruby-devel rubygems puppet git supervisord mosh
git-core zlib zlib-devel gcc-c++ patch readline readline-devel libyaml-devel
libffi-devel openssl-devel make bzip2 autoconf automake libtool bison curl
sqlite-devel&& \  
yum clean all  
  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN /root/.rbenv/plugins/ruby-build/install.sh  
#RUN "export PATH=$PATH:/opt/puppetlabs/puppet/bin/:/root/.rbenv/bin/"  
ENV PATH "$PATH:/opt/puppetlabs/puppet/bin/:/root/.rbenv/bin/"  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> .bashrc  
  
# Install multiple versions of ruby  
ENV CONFIGURE_OPTS --disable-install-doc  
COPY ruby_versions.txt /root/versions.txt  
RUN cat /root/versions.txt  
RUN xargs -L 1 rbenv install < /root/versions.txt  
RUN echo 'gem: --no-rdoc --no-ri' >> /root/.gemrc  
RUN bash -l -c 'for v in $(cat /root/versions.txt); do rbenv global $v; gem
install bundler librarian-puppet; done'  

