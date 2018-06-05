FROM ubuntu:14.04  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install basic dev tools  
RUN apt-get update && apt-get install -y \  
build-essential \  
wget \  
curl \  
git \  
zlib1g-dev \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libxml2-dev \  
libxslt-dev \  
libmagickwand-dev \  
imagemagick \  
rubygems-integration  
  
# Install rbenv and ruby-build  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN echo 'eval "$(rbenv init -)"' >> /root/.bashrc  
ENV PATH /root/.rbenv/bin:/.rbenv/bin:/.rbenv/shims:/root/.rbenv/shims:$PATH  
RUN echo PATH=$PATH  
RUN exec $SHELL  
RUN /root/.rbenv/bin/rbenv init -  
  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN /root/.rbenv/plugins/ruby-build/install.sh  
RUN echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >>
/root/.bashrc  
ENV PATH $HOME/.rbenv/plugins/ruby-build/bin:$PATH  
RUN exec $SHELL  
RUN echo PATH=$PATH  
  
RUN rbenv install 2.1.5 && rbenv global 2.1.5 && gem update && gem install
bundler  
  
# Add Application  
RUN mkdir /myapp  
WORKDIR /myapp  
ADD . /myapp  
RUN bundle install  
  
EXPOSE 4567  
CMD ["bundle", "exec", "rackup", "-p", "4567"]  
  

