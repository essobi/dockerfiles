FROM ubuntu:wily  
MAINTAINER "Pedro Cesar" <pedrocesar.ti@gmail.com>  
EXPOSE 4567  
# INSTALL BASE TOOLS  
RUN apt-get update  
RUN apt-get install -y --force-yes build-essential curl git nodejs  
RUN apt-get install -y --force-yes zlib1g-dev libssl-dev libreadline-dev
libyaml-dev libxml2-dev libxslt-dev  
RUN apt-get clean  
  
# INSTALL AND CONFIGURE RUBY  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv  
RUN git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build  
RUN /root/.rbenv/plugins/ruby-build/install.sh  
ENV PATH /root/.rbenv/shims:/root/.rbenv/bin:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> .bashrc  
ENV CONFIGURE_OPTS --disable-install-doc  
RUN rbenv install 2.1.0  
RUN rbenv global 2.1.0  
RUN gem install --no-ri --no-rdoc bundler  
  
# CONFIGURE BASE APPLICATION  
RUN mkdir -p /app/slate  
ADD slate/ /app/slate/  
RUN cd /app/slate/; bundle install  
WORKDIR /app/slate  
  
# BOOTSTRAP  
ONBUILD ADD . /app/source/slate  
CMD ["bundle", "exec", "middleman", "server"]  
  

