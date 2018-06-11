FROM phusion/baseimage:0.9.15  
  
ENV HOME /root  
  
CMD ["/sbin/my_init"]  
  
RUN apt-get -y update &&\  
apt-get -y install build-essential zlib1g-dev libssl-dev libreadline6-dev
libyaml-dev wget &&\  
cd /tmp &&\  
wget http://ftp.ruby-lang.org/pub/ruby/2.1/ruby-2.1.3.tar.gz &&\  
tar -xvzf ruby-2.1.3.tar.gz &&\  
cd ruby-2.1.3/ &&\  
./configure --prefix=/usr/local &&\  
make &&\  
make install &&\  
make clean  
  
ENV PATH /opt/rubies/ruby-2.1.3/bin:$PATH  
  
RUN echo "gem: --no-document" > ~/.gemrc &&\  
gem install bundler &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

