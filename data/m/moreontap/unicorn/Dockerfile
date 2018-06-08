FROM fedora:21  
MAINTAINER Jordan Ryan Reuter <jordan@moreontap.com>  
  
RUN yum -y install \  
gcc \  
gdbm-devel \  
git \  
libffi-devel \  
libyaml-devel \  
make \  
mysql-devel \  
ncurses-devel \  
openssl-devel \  
readline-devel \  
tar \  
zlib-devel  
  
WORKDIR ~  
RUN git clone https://github.com/sstephenson/ruby-build.git  
RUN ./ruby-build/install.sh  
  
ENV APP_RUBY_VERSION '2.2.1'  
RUN ruby-build $APP_RUBY_VERSION /usr/local/ruby  
ENV PATH /usr/local/ruby/bin:$PATH  
RUN gem install \  
bundler \  
unicorn  
  
RUN mkdir -p /etc/unicorn  
  
ONBUILD COPY application /application  
ONBUILD WORKDIR /application  
  
ONBUILD RUN bundle install  
  
ONBUILD RUN ln -sf /dev/stdout /etc/unicorn/access.log  
ONBUILD RUN ln -sf /dev/stderr /etc/unicorn/error.log  
  
EXPOSE 3000  
CMD ["bundle", "exec", "unicorn", "-c", "unicorn.rb"]  

