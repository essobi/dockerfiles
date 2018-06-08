FROM ubuntu:utopic  
  
# turn on universe packages  
#RUN echo "deb http://archive.ubuntu.com/ubuntu raring main universe" >
/etc/apt/sources.list  
RUN apt-get update  
  
# basics  
RUN apt-get install -y openssh-server git-core openssh-client curl ruby build-
essential openssl libreadline6 libreadline6-dev curl zlib1g zlib1g-dev libssl-
dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt-dev autoconf
libc6-dev ncurses-dev automake libtool bison subversion pkg-config gawk
libgdbm-dev libffi-dev npm clang llvm llvm-dev  
RUN apt-get clean  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# Generate and set UTF-8 locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# install RVM, Ruby, and Bundler  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
RUN \curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install rbx"  
RUN /bin/bash -l -c "rvm use rbx --default"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
  

