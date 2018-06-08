FROM ubuntu:trusty  
MAINTAINER bartek@procreative.eu  
  
RUN mkdir -p /app  
WORKDIR /app  
  
RUN apt-get update && \  
apt-get install -y autoconf \  
bison \  
build-essential \  
curl \  
git \  
libffi-dev \  
libgdbm-dev \  
libgdbm3 \  
libncurses5-dev \  
libpq-dev \  
libreadline6-dev \  
libssl-dev \  
libyaml-dev \  
nodejs \  
libsqlite3-dev \  
zlib1g-dev && \  
apt-get autoremove -y && \  
apt-get clean  
  
  
RUN git clone --depth 1 https://github.com/sstephenson/rbenv.git /root/.rbenv
&& \  
git clone --depth 1 https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build && \  
rm -rfv /root/.rbenv/plugins/ruby-build/.git && \  
rm -rfv /root/.rbenv/.git && \  
export PATH="/root/.rbenv/bin:$PATH" && \  
eval "$(rbenv init -)" && \  
rbenv install '2.3.0' && \  
rbenv global '2.3.0' && \  
gem install bundler --no-ri --no-rdoc && \  
rbenv rehash && \  
gem install rails -v '>= 5.0.0.beta3' \--no-ri --no-rdoc && \  
rbenv rehash  
  
ENV PATH /root/.rbenv/bin:/root/.rbenv/shims:$PATH  
RUN echo "export PATH=$PATH" >> /root/.bashrc  
RUN rails new test-app && \  
mv test-app/* .  
  
CMD ["rails", "server", "-b", "0.0.0.0"]  
  
EXPOSE 3000  

