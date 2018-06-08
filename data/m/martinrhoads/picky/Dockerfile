FROM stackbrew/ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y \  
autoconf\  
bison\  
build-essential\  
curl\  
git\  
libssl-dev\  
libyaml-dev\  
libreadline6-dev\  
libncurses5-dev\  
libffi-dev\  
libgdbm3\  
libgdbm-dev\  
zlib1g-dev  
  
# install rbenv && ruby2  
RUN git clone https://github.com/sstephenson/rbenv.git ~/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
~/.rbenv/plugins/ruby-build  
RUN echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc  
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc  
RUN /root/.rbenv/bin/rbenv install 2.1.3  
RUN /root/.rbenv/bin/rbenv global 2.1.3  
RUN /root/.rbenv/shims/gem install bundler  
  
ADD Gemfile /root/martin/Gemfile  
ADD Gemfile.lock /root/martin/Gemfile.lock  
WORKDIR /root/martin  
RUN apt-get install -y libxml2-dev  
RUN apt-get install -y libxslt1-dev  
RUN /root/.rbenv/shims/bundle install  
  
ADD sinatra.rb /root/martin/sinatra.rb  
  
RUN apt-get install -y tmux  
EXPOSE 4567  
# CMD /root/.rbenv/shims/ruby sinatra.rb  

