from java  
  
# install ruby 2.1.5  
# instructions from https://stackoverflow.com/questions/18490591/how-to-
install-ruby-2-on-ubuntu-without-rvm?answertab=active#tab-top  
workdir /tmp  
run \  
apt-get -y update && \  
apt-get -y install wget build-essential zlib1g-dev libssl-dev libreadline6-dev
libyaml-dev && \  
wget http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.5.tar.gz  
  
run \  
tar -xvzf ruby-2.1.5.tar.gz && \  
cd ruby-2.1.5/ && \  
./configure --prefix=/usr/local && \  
make && \  
make install  
  
run \  
gem install bundler  
  
# install sox and mp3 format support  
run \  
apt-get -y install libsox-fmt-mp3 sox  
  
# copy the application files to the image  
workdir /srv/tomecast-worker  
copy . /srv/tomecast-worker  
run bundle install --path vendor/bundle  
  
#finish up  
cmd ["bundle", "exec", "sidekiq", "-r", "./worker.rb", "-c","1"]  
#"bundle", "exec", "ruby", "processor.rb"

