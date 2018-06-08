FROM ubuntu-debootstrap:14.04  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
automake \  
bison \  
build-essential \  
bzip2 \  
ca-certificates \  
clang \  
cpio \  
curl \  
debhelper \  
file \  
g++-multilib \  
gcc-multilib \  
genisoimage \  
git \  
gobject-introspection \  
gzip \  
intltool \  
libgirepository1.0-dev \  
libgsf-1-dev \  
libssl-dev \  
libtool \  
libxml2-dev \  
llvm-dev \  
make \  
mingw-w64 \  
patch \  
rpm \  
sed \  
uuid-dev \  
valac \  
wget \  
xz-utils  
  
# install ruby  
RUN mkdir -p /opt/ruby-2.2.2/ && \  
curl -s https://s3-external-1.amazonaws.com/heroku-buildpack-
ruby/cedar-14/ruby-2.2.2.tgz | tar xzC /opt/ruby-2.2.2/  
ENV PATH /opt/ruby-2.2.2/bin:$PATH  
  
# install fpm to build packages (deb, rpm)  
RUN gem install fpm --no-document  
  
  
ONBUILD WORKDIR /home/mruby/code  
ONBUILD ENV GEM_HOME /home/mruby/.gem/  
  
ONBUILD ENV PATH $GEM_HOME/bin/:$PATH  
ONBUILD ENV LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib/  

