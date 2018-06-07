# Test image created during practice. Since ruby repo contains 1.x version
only, install 2.x version from source.  
FROM ubuntu:14.04  
MAINTAINER Timur Hilmutdinov <t.gilmutdinov@gmail.com>  
RUN apt-get update ;\  
apt-get install -y git-core curl zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev python-software-properties libffi-dev  
RUN git clone git://github.com/sstephenson/rbenv.git ~/.rbenv ;\  
git clone git://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-
build  
RUN echo 'export PATH="~/.rbenv/bin:$PATH"' >> ~/.bashrc ;\  
echo 'eval "$(rbenv init -)"' >> ~/.bashrc ;\  
echo 'export PATH="~/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc ;\  
eval "$(.rbenv/bin/rbenv init -)"  
RUN ~/.rbenv/bin/rbenv install 2.2.0 ;\  
~/.rbenv/bin/rbenv global 2.2.0 ;\  
~/.rbenv/shims/gem install sinatra  
CMD ["bin/bash"]  

