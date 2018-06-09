FROM ubuntu:14.04  
MAINTAINER Grant Callaghan <grant@brkt.com>  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
git \  
wget \  
bison \  
openssl \  
libreadline6 \  
libreadline6-dev \  
git-core \  
zlib1g \  
zlib1g-dev \  
libssl-dev \  
libyaml-dev \  
libxml2-dev \  
libgdbm3 \  
libgdbm-dev \  
autoconf \  
libxslt-dev \  
libc6-dev \  
ncurses-dev \  
automake \  
pkg-config \  
subversion \  
libtool \  
libffi-dev \  
libncurses5-dev \  
ImageMagick \  
GraphicsMagick \  
pngquant \  
python-dev \  
python-support \  
unzip \  
python-setuptools \  
python-pip  
  
RUN cd /tmp; \  
wget http://cache.ruby-lang.org/pub/ruby/2.2/ruby-2.2.2.tar.gz; \  
tar -xvzf ruby-2.2.2.tar.gz; cd ruby-2.2.2; CFLAGS=-fPIC; \  
./configure; make && make install; \  
ln -s /usr/local/bin/ruby /usr/bin/ruby; \  
gem install bundle  
  
RUN cd /tmp; \  
wget http://nodejs.org/dist/v0.12.4/node-v0.12.4.tar.gz; \  
tar -xvzf node-v0.12.4.tar.gz; cd node-v0.12.4; \  
./configure; make && make install  
  
RUN npm config set registry http://registry.npmjs.org/  
RUN npm install -g grunt-cli grunt-image  
RUN pip install awscli  
  
RUN mkdir -p /work/brkt-public  
WORKDIR /work/brkt-public  
ADD Gemfile /work/brkt-public/Gemfile  
RUN echo "Bundle install!!!"  
RUN bundle install  
  
ADD package.json /work/brkt-public/package.json  
RUN rm -fr node_modules  
RUN npm install  
  
ADD ./ /work/brkt-public/  
  
EXPOSE 8000  
ENTRYPOINT ["python", "/work/brkt-public/dev-init.py"]  
CMD ["--help"]  

