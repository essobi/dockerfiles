FROM ubuntu:14.04  
ENV RUBY_VERSION 2.3.0  
ENV HOME /root  
# Add repositoroes and install dependencies  
RUN apt-get update && apt-get install -y git-core curl zlib1g-dev build-
essential libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3
libxml2-dev libxslt1-dev libcurl4-openssl-dev python-software-properties
libffi-dev wget unzip  
  
# Install rbenv and ruby-build  
RUN git clone https://github.com/rbenv/rbenv.git $HOME/.rbenv  
RUN git clone https://github.com/rbenv/ruby-build.git
$HOME/.rbenv/plugins/ruby-build  
RUN $HOME/.rbenv/plugins/ruby-build/install.sh  
ENV PATH $HOME/.rbenv/bin:$HOME/.rbenv/shims:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> $HOME/.bashrc  
  
RUN rbenv install $RUBY_VERSION && rbenv global $RUBY_VERSION  
  
RUN gem install bundler  
  
RUN /bin/bash -c "wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh"  

