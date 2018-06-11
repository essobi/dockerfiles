FROM ubuntu:16.04  
# for building ruby  
RUN apt-get -qq update && \  
apt-get -qqy install \  
build-essential \  
curl \  
git \  
zlib1g-dev \  
libssl-dev \  
libreadline-dev \  
libyaml-dev \  
libxml2-dev \  
libcurl4-gnutls-dev \  
libxslt-dev \  
# for postgresql  
libpq-dev \  
postgresql-client \  
# for clamAV  
libpcre3 \  
libpcre3-dev \  
libncurses5-dev \  
unrar-free \  
libzip-dev \  
bzip2 \  
libbz2-dev && \  
apt-get clean  
  
# Install rbenv and ruby-build  
RUN git clone https://github.com/sstephenson/rbenv.git /root/.rbenv && \  
git clone https://github.com/sstephenson/ruby-build.git
/root/.rbenv/plugins/ruby-build && \  
/root/.rbenv/plugins/ruby-build/install.sh  
  
# compile rbenv  
RUN cd /root/.rbenv && src/configure && make -C src  
  
# rbenv path  
ENV PATH /root/.rbenv/bin:/root/.rbenv/shims:$PATH  
RUN echo 'eval "$(rbenv init -)"' >> /etc/profile.d/rbenv.sh # or /etc/profile  
RUN echo 'eval "$(rbenv init -)"' >> ~/.bashrc  
  
# nodoc  
RUN echo 'gem: --no-rdoc --no-ri' >> ~/.gemrc  
  
# install ruby  
RUN rbenv install 2.3.1 && \  
rbenv global 2.3.1 && \  
ruby -v  
  
# install bundler  
RUN gem install bundler  
  
# config clamav user  
RUN useradd -ms /bin/bash clamav  
RUN mkdir /var/lib/clamav  
RUN chown clamav:clamav -R /var/lib/clamav  
  
# build clamav  
RUN cd /usr/src && \  
curl -LO https://www.clamav.net/downloads/production/clamav-0.99.2.tar.gz && \  
tar xzvf clamav-0.99.2.tar.gz && \  
cd clamav-0.99.2 && \  
./configure --enable-bzip2 --with-system-llvm --disable-llvm -q && make
CFLAGS="-Wall -g -O2 -Wno-unused-variable -Wno-unused-value" -s && \  
make install -s  
  
# clean clamav  
RUN cd /usr/src && \  
rm -rf clamav-0.99.2*  
  
# link shared libraries  
RUN ldconfig  
  
# ClamAV  
COPY config/freshclam.conf /usr/local/etc/freshclam.conf  
RUN chmod 0700 /usr/local/etc/freshclam.conf  
COPY config/clamd.conf /usr/local/etc/clamd.conf  
#RUN freshclam -v  
RUN clamscan --version > CLAM_VERSION  

