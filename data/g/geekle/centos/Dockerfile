FROM centos  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN yum install -y git gcc tar openssl-devel gcc-c++ readline-devel sqlite-
devel  
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv  
RUN mkdir -p ~/.rbenv/plugins && git clone
https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build  
RUN echo -e 'export PATH=~/.rbenv/bin:$PATH\neval "$(rbenv init -)"' >>
/etc/profile.d/rbenv.sh && source /etc/profile.d/rbenv.sh  
RUN bash -lc 'CONFIGURE_OPTS="--disable-install-doc" ~/.rbenv/plugins/ruby-
build/bin/ruby-build 2.1.1 ~/.rbenv/versions/2.1.1'  
RUN echo 'gem: --no-rdoc --no-ri' >> /.gemrc  
RUN bash -lc 'rbenv global 2.1.1; gem install bundler; rbenv rehash'  
#Add Gemfile ruby version  
RUN git clone https://github.com/aripollak/rbenv-bundler-ruby-version.git
~/.rbenv/plugins/rbenv-bundler-ruby-version  

