FROM centos:6  
MAINTAINER Tim Ehlers <ehlerst@gmail.com>  
  
ENV RUBY_VERSION 2.4.0  
ENV PATH $PATH:/usr/local/rvm/bin  
ENV PATH $PATH:/usr/local/go/bin  
  
USER root  
  
RUN yum install git -y  
  
RUN yum install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-6.noarch.rpm -y  
  
RUN yum groupinstall 'Development Tools' -y  
  
RUN yum install openssl-devel zlib-devel python wget -y  
  
RUN mkdir -p ~/rpmbuild/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}  
  
### Update go to a newer version of go  
RUN wget https://storage.googleapis.com/golang/go1.8.linux-amd64.tar.gz  
  
RUN tar -C /usr/local -xzf go1.8.linux-amd64.tar.gz  
  
### Update to a newer version of ruby  
# install RVM, Ruby, and Bundler  
RUN /bin/bash -l -c "gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3 && \curl -L https://get.rvm.io |
/bin/bash -s stable"  
RUN /bin/bash -lc "rvm requirements"  
  
RUN /bin/bash -lc "rvm install ${RUBY_VERSION} && rvm use ${RUBY_VERSION}
\--default"  
RUN /bin/bash -lc "rvm install ${RUBY_VERSION}-dev"  
  
RUN rvm rubygems current  
  
RUN /bin/bash -lc "gem install rubocop pleaserun fpm"  

