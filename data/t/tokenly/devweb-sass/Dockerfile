### Dockerfile  
# Tokenly Development Image for web apps  
# Adds Ruby/Sass to the tokenly/devweb image  
FROM tokenly/devweb  
MAINTAINER Devon Weller <devon@tokenly.com>  
  
# pre-reqs  
RUN apt-get update  
RUN apt-get -y install git-core curl zlib1g-dev build-essential libssl-dev
libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev libxslt1-dev
libcurl4-openssl-dev python-software-properties libgdbm-dev libncurses5-dev
automake libtool bison libffi-dev  
  
# build ruby  
RUN github="https://github.com/sstephenson" && \  
git clone \--depth=1 $github/rbenv.git /.rbenv && \  
git clone \--depth=1 $github/ruby-build.git /.rbenv/plugins/ruby-build  
ENV PATH /.rbenv/bin:/.rbenv/shims:$PATH  
ENV RBENV_ROOT /.rbenv  
RUN /.rbenv/plugins/ruby-build/install.sh && \  
echo 'eval "$(rbenv init -)"' >> /.bashrc && \  
echo "gem: --no-rdoc --no-ri" >> /.gemrc  
RUN version="2.1.9" && \  
rbenv install $version && \  
rbenv global $version  
RUN gem install bundler && \  
rbenv rehash  
  
# install sass  
RUN gem install sass  
RUN ruby --version && sass --version  
  
# clean up apt-get artifacts  
RUN rm -rf /var/lib/apt/lists/*  
  

