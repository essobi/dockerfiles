FROM groupbuddies/nginx:latest  
MAINTAINER naps62 <mpalhas@groupbuddies.com>  
  
RUN apt-get update && apt-get install -y build-essential libssl-dev git-core
curl postgresql-client libpq-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV RUBY_MAJOR 2.1  
ENV RUBY_VERSION 2.1.5  
WORKDIR /tmp/ruby-build  
RUN git clone https://github.com/sstephenson/ruby-build .  
RUN git checkout v20141113  
RUN ./install.sh  
RUN ruby-build 2.1.5 /usr/local  
  
# skip installing gem documentation  
RUN echo 'gem: --no-rdoc --no-ri' >> "$HOME/.gemrc"  
  
# install things globally, for great justice  
ENV GEM_HOME /usr/local/bundle  
ENV PATH $GEM_HOME/bin:$PATH  
RUN gem install bundler \  
&& bundle config --global path "$GEM_HOME" \  
&& bundle config --global bin "$GEM_HOME/bin"  
  
WORKDIR /usr/src/app  

